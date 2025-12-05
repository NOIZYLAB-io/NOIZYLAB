const vscode = require('vscode')
const path = require('path')
const fsPromises = require('fs').promises

/**
 * DiffManager - Manages diff preview sessions with streaming support
 * Provides real-time visual feedback as code changes are being applied
 */
class DiffManager {
  constructor() {
    this.activeSessions = new Map()
    this.decorationTypes = {
      added: vscode.window.createTextEditorDecorationType({
        backgroundColor: 'rgba(0, 255, 0, 0.15)',
        isWholeLine: true
      }),
      modified: vscode.window.createTextEditorDecorationType({
        backgroundColor: 'rgba(255, 255, 0, 0.15)',
        isWholeLine: true
      }),
      deleted: vscode.window.createTextEditorDecorationType({
        backgroundColor: 'rgba(255, 0, 0, 0.15)',
        textDecoration: 'line-through',
        isWholeLine: true
      }),
      currentLine: vscode.window.createTextEditorDecorationType({
        backgroundColor: 'rgba(255, 255, 0, 0.3)',
        border: '1px solid rgba(255, 255, 0, 0.5)',
        isWholeLine: true
      }),
      fadedOverlay: vscode.window.createTextEditorDecorationType({
        opacity: '0.4',
        isWholeLine: true
      })
    }
  }

  async startSession(sessionId, filePath, initialContent = '') {
    try {
      if (!vscode.workspace.rootPath) {
        throw new Error('No workspace folder is open')
      }

      const absolutePath = path.isAbsolute(filePath)
        ? filePath
        : path.join(vscode.workspace.rootPath, filePath)

      let originalContent = ''
      let fileExists = false
      try {
        originalContent = await fsPromises.readFile(absolutePath, 'utf8')
        fileExists = true
      } catch (error) {
        const dir = path.dirname(absolutePath)
        await fsPromises.mkdir(dir, { recursive: true })
      }

      const originalUri = vscode.Uri.from({
        scheme: 'codegpt-diff',
        path: path.basename(filePath),
        query: Buffer.from(originalContent).toString('base64')
      })

      if (!fileExists) {
        await fsPromises.writeFile(absolutePath, initialContent || '')
      }

      const modifiedUri = vscode.Uri.file(absolutePath)

      await vscode.commands.executeCommand(
        'vscode.diff',
        originalUri,
        modifiedUri,
        `Preview: ${path.basename(filePath)} - Original ↔ Changes`,
        { preview: false, preserveFocus: false }
      )

      await new Promise((resolve) => setTimeout(resolve, 200))

      const editor = vscode.window.activeTextEditor

      this.activeSessions.set(sessionId, {
        filePath: absolutePath,
        originalContent,
        editor,
        streamedLines: [],
        currentLine: 0,
        accumulatedContent: initialContent || ''
      })

      return {
        success: true,
        sessionId,
        filePath: absolutePath
      }
    } catch (error) {
      return {
        success: false,
        error: error.message
      }
    }
  }

  async streamUpdate(sessionId, content, isPartial = true) {
    const session = this.activeSessions.get(sessionId)
    if (!session) {
      return { success: false, error: 'Session not found' }
    }

    try {
      if (!isPartial) {
        session.accumulatedContent = content
      } else {
        session.accumulatedContent += content
      }

      await fsPromises.writeFile(session.filePath, session.accumulatedContent)

      if (session.editor && !session.editor.document.isClosed) {
        const lines = session.accumulatedContent.split('\n')
        const currentLine = Math.max(0, lines.length - 2)

        this.applyStreamingDecorations(session.editor, currentLine, lines.length)

        if (currentLine > session.currentLine) {
          await this.smoothScroll(session.editor, session.currentLine, currentLine)
          session.currentLine = currentLine
        }
      }

      return { success: true }
    } catch (error) {
      return { success: false, error: error.message }
    }
  }

  async completeSession(sessionId, finalContent = null) {
    const session = this.activeSessions.get(sessionId)
    if (!session) {
      return { success: false, error: 'Session not found' }
    }

    try {
      if (finalContent !== null) {
        await fsPromises.writeFile(session.filePath, finalContent)
      }

      if (session.editor && !session.editor.document.isClosed) {
        this.clearDecorations(session.editor)
      }

      const document = await vscode.workspace.openTextDocument(session.filePath)
      await document.save()

      await this.closeDiffView(session)

      this.activeSessions.delete(sessionId)

      // deja el archivo definitivo abierto
      await vscode.window.showTextDocument(document, vscode.ViewColumn.Active, false)

      return { success: true, message: 'Diff preview completed successfully' }
    } catch (error) {
      return { success: false, error: error.message }
    }
  }

  async cancelSession(sessionId) {
    const session = this.activeSessions.get(sessionId)
    if (!session) {
      return { success: false, error: 'Session not found' }
    }

    try {
      await fsPromises.writeFile(session.filePath, session.originalContent)

      if (session.editor && !session.editor.document.isClosed) {
        this.clearDecorations(session.editor)
      }

      await this.closeDiffView(session)

      this.activeSessions.delete(sessionId)

      return {
        success: true,
        message: 'Diff preview cancelled, changes reverted'
      }
    } catch (error) {
      return { success: false, error: error.message }
    }
  }

  async closeDiffView(session) {
    const diffUri = vscode.Uri.from({
      scheme: 'codegpt-diff',
      path: path.basename(session.filePath),
      query: Buffer.from(session.originalContent).toString('base64')
    })

    // Reabre el diff en modo preview para asegurarnos de que sea el activo
    await vscode.commands.executeCommand(
      'vscode.diff',
      diffUri,
      vscode.Uri.file(session.filePath),
      `Preview: ${path.basename(session.filePath)} - Original ↔ Changes`,
      { preview: true, preserveFocus: false }
    )

    // Cierra el editor activo (el diff recién abierto)
    await vscode.commands.executeCommand('workbench.action.closeActiveEditor')
  }

  getActiveSessions() {
    return Array.from(this.activeSessions.keys())
  }

  async cleanup() {
    for (const sessionId of this.activeSessions.keys()) {
      await this.cancelSession(sessionId)
    }
  }

  applyStreamingDecorations(editor, currentLine, totalLines) {
    if (!editor) return

    Object.values(this.decorationTypes).forEach((decoration) => {
      editor.setDecorations(decoration, [])
    })

    editor.setDecorations(this.decorationTypes.currentLine, [
      new vscode.Range(currentLine, 0, currentLine, Number.MAX_SAFE_INTEGER)
    ])

    if (currentLine < totalLines - 1) {
      const fadedRanges = []
      for (let i = currentLine + 1; i < totalLines; i++) {
        fadedRanges.push(new vscode.Range(i, 0, i, Number.MAX_SAFE_INTEGER))
      }
      editor.setDecorations(this.decorationTypes.fadedOverlay, fadedRanges)
    }
  }

  clearDecorations(editor) {
    if (!editor) return
    Object.values(this.decorationTypes).forEach((decoration) => {
      editor.setDecorations(decoration, [])
    })
  }

  async smoothScroll(editor, startLine, endLine) {
    if (!editor) return

    const totalLines = endLine - startLine
    const steps = Math.min(10, totalLines)
    const stepSize = Math.max(1, Math.floor(totalLines / steps))

    for (let line = startLine; line <= endLine; line += stepSize) {
      editor.revealRange(new vscode.Range(line, 0, line, 0), vscode.TextEditorRevealType.InCenter)
      await new Promise((resolve) => setTimeout(resolve, 16))
    }

    editor.revealRange(
      new vscode.Range(endLine, 0, endLine, 0),
      vscode.TextEditorRevealType.InCenter
    )
  }
}

module.exports = DiffManager
