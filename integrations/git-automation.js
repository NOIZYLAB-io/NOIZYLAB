// ═══════════════════════════════════════════════════════════════════════════════
// GIT AUTOMATION - INTELLIGENT VERSION CONTROL
// Auto-commit, smart branching, PR creation, and more
// ═══════════════════════════════════════════════════════════════════════════════

import { execSync } from "child_process";

export class GitAutomation {
  constructor(options = {}) {
    this.cwd = options.cwd || process.cwd();
    this.aiRouter = options.aiRouter || null;
    this.config = {
      defaultBranch: "main",
      branchPrefix: "feature/",
      commitTypes: ["feat", "fix", "docs", "style", "refactor", "test", "chore"],
      ...options.config
    };
  }

  // ─── HELPERS ───────────────────────────────────────────────────────────────

  exec(cmd) {
    try {
      return execSync(cmd, { cwd: this.cwd, encoding: "utf8" }).trim();
    } catch (error) {
      throw new Error(`Git command failed: ${cmd}\n${error.message}`);
    }
  }

  execSafe(cmd) {
    try {
      return execSync(cmd, { cwd: this.cwd, encoding: "utf8" }).trim();
    } catch {
      return null;
    }
  }

  // ─── STATUS & INFO ─────────────────────────────────────────────────────────

  status() {
    const branch = this.getCurrentBranch();
    const status = this.exec("git status --porcelain");
    const ahead = this.execSafe("git rev-list --count @{u}..HEAD") || "0";
    const behind = this.execSafe("git rev-list --count HEAD..@{u}") || "0";

    const files = status.split("\n").filter(Boolean).map(line => ({
      status: line.substring(0, 2).trim(),
      file: line.substring(3)
    }));

    const staged = files.filter(f => ["A", "M", "D", "R"].includes(f.status[0]));
    const unstaged = files.filter(f => ["M", "D"].includes(f.status[1]) || f.status === "??");

    return {
      branch,
      ahead: parseInt(ahead),
      behind: parseInt(behind),
      staged: staged.length,
      unstaged: unstaged.length,
      files,
      clean: files.length === 0
    };
  }

  getCurrentBranch() {
    return this.exec("git branch --show-current");
  }

  getRemoteUrl() {
    return this.execSafe("git config --get remote.origin.url");
  }

  getLastCommit() {
    const hash = this.exec("git rev-parse --short HEAD");
    const message = this.exec("git log -1 --pretty=%B").trim();
    const author = this.exec("git log -1 --pretty=%an");
    const date = this.exec("git log -1 --pretty=%ci");

    return { hash, message, author, date };
  }

  getRecentCommits(count = 10) {
    const log = this.exec(`git log -${count} --pretty=format:"%h|%s|%an|%ci"`);
    return log.split("\n").map(line => {
      const [hash, message, author, date] = line.split("|");
      return { hash, message, author, date };
    });
  }

  // ─── BRANCH MANAGEMENT ─────────────────────────────────────────────────────

  listBranches() {
    const local = this.exec("git branch").split("\n").map(b => b.replace("*", "").trim());
    const remote = this.execSafe("git branch -r")?.split("\n").map(b => b.trim()) || [];

    return {
      current: this.getCurrentBranch(),
      local,
      remote
    };
  }

  createBranch(name, options = {}) {
    const { checkout = true, from = null } = options;

    // Apply prefix if not already present
    const branchName = name.startsWith(this.config.branchPrefix)
      ? name
      : `${this.config.branchPrefix}${name}`;

    if (from) {
      this.exec(`git branch ${branchName} ${from}`);
    } else {
      this.exec(`git branch ${branchName}`);
    }

    if (checkout) {
      this.exec(`git checkout ${branchName}`);
    }

    return branchName;
  }

  checkout(branch) {
    this.exec(`git checkout ${branch}`);
    return this.status();
  }

  deleteBranch(branch, options = {}) {
    const { force = false, remote = false } = options;

    const flag = force ? "-D" : "-d";
    this.exec(`git branch ${flag} ${branch}`);

    if (remote) {
      this.execSafe(`git push origin --delete ${branch}`);
    }
  }

  mergeBranch(source, options = {}) {
    const { noFf = false, squash = false } = options;

    let cmd = `git merge ${source}`;
    if (noFf) cmd += " --no-ff";
    if (squash) cmd += " --squash";

    return this.exec(cmd);
  }

  // ─── SMART COMMIT ──────────────────────────────────────────────────────────

  async smartCommit(options = {}) {
    const { message, type = "auto", scope = null, ai = true } = options;

    // Get changes
    const diff = this.getDiff({ staged: true });

    if (!diff) {
      throw new Error("No staged changes to commit");
    }

    let commitMessage = message;

    // Generate message with AI if not provided
    if (!commitMessage && ai && this.aiRouter) {
      commitMessage = await this.generateCommitMessage(diff);
    }

    if (!commitMessage) {
      throw new Error("Commit message required");
    }

    // Format conventional commit
    if (type !== "auto" && this.config.commitTypes.includes(type)) {
      const scopePart = scope ? `(${scope})` : "";
      commitMessage = `${type}${scopePart}: ${commitMessage}`;
    }

    // Execute commit
    this.exec(`git commit -m "${commitMessage.replace(/"/g, '\\"')}"`);

    return {
      message: commitMessage,
      hash: this.exec("git rev-parse --short HEAD"),
      timestamp: new Date().toISOString()
    };
  }

  async generateCommitMessage(diff) {
    if (!this.aiRouter) {
      throw new Error("AI Router required for message generation");
    }

    const prompt = `Generate a concise, conventional commit message for these changes:

${diff.substring(0, 3000)}

Rules:
- Start with type: feat, fix, docs, style, refactor, test, or chore
- Be specific but concise (max 72 chars for first line)
- Focus on WHAT changed, not HOW

Return only the commit message, nothing else.`;

    const result = await this.aiRouter.run(prompt, { model: "mistral" });
    return result.response.trim().replace(/^["']|["']$/g, "");
  }

  // ─── STAGING ───────────────────────────────────────────────────────────────

  stage(files = []) {
    if (files.length === 0) {
      this.exec("git add -A");
    } else {
      files.forEach(file => {
        this.exec(`git add "${file}"`);
      });
    }
    return this.status();
  }

  unstage(files = []) {
    if (files.length === 0) {
      this.exec("git reset HEAD");
    } else {
      files.forEach(file => {
        this.exec(`git reset HEAD "${file}"`);
      });
    }
    return this.status();
  }

  // ─── DIFF ──────────────────────────────────────────────────────────────────

  getDiff(options = {}) {
    const { staged = false, file = null } = options;

    let cmd = "git diff";
    if (staged) cmd += " --staged";
    if (file) cmd += ` -- "${file}"`;

    return this.execSafe(cmd);
  }

  getDiffStats() {
    const stats = this.execSafe("git diff --stat");
    const summary = this.execSafe("git diff --shortstat");

    return { stats, summary };
  }

  // ─── REMOTE OPERATIONS ─────────────────────────────────────────────────────

  push(options = {}) {
    const { branch = null, setUpstream = false, force = false } = options;

    let cmd = "git push";
    if (setUpstream) cmd += " -u origin";
    if (branch) cmd += ` origin ${branch}`;
    if (force) cmd += " --force";

    return this.exec(cmd);
  }

  pull(options = {}) {
    const { rebase = false } = options;

    let cmd = "git pull";
    if (rebase) cmd += " --rebase";

    return this.exec(cmd);
  }

  fetch(options = {}) {
    const { all = false, prune = false } = options;

    let cmd = "git fetch";
    if (all) cmd += " --all";
    if (prune) cmd += " --prune";

    return this.exec(cmd);
  }

  // ─── STASH ─────────────────────────────────────────────────────────────────

  stash(message = null) {
    let cmd = "git stash";
    if (message) cmd += ` push -m "${message}"`;
    return this.exec(cmd);
  }

  stashPop() {
    return this.exec("git stash pop");
  }

  stashList() {
    const list = this.execSafe("git stash list");
    if (!list) return [];

    return list.split("\n").map((line, index) => {
      const match = line.match(/stash@\{(\d+)\}: (.+)/);
      return {
        index,
        ref: `stash@{${index}}`,
        message: match ? match[2] : line
      };
    });
  }

  // ─── PR CREATION ───────────────────────────────────────────────────────────

  async createPR(options = {}) {
    const {
      title,
      body,
      base = this.config.defaultBranch,
      draft = false,
      ai = true
    } = options;

    const branch = this.getCurrentBranch();

    // Ensure changes are pushed
    this.push({ setUpstream: true, branch });

    // Get commits for this branch
    const commits = this.exec(`git log ${base}..HEAD --pretty=format:"%s"`);
    const diff = this.execSafe(`git diff ${base}...HEAD --stat`);

    // Generate PR body with AI if not provided
    let prBody = body;

    if (!prBody && ai && this.aiRouter) {
      const prompt = `Generate a PR description for these changes:

Branch: ${branch}
Base: ${base}

Commits:
${commits}

Changed files:
${diff}

Format:
## Summary
[Brief description]

## Changes
- [Change 1]
- [Change 2]

## Testing
- [ ] Tests pass
- [ ] Manual testing done`;

      const result = await this.aiRouter.run(prompt, { model: "mistral" });
      prBody = result.response;
    }

    // Return PR data (actual creation would need GitHub API)
    return {
      branch,
      base,
      title: title || `Merge ${branch} into ${base}`,
      body: prBody,
      draft,
      commits: commits.split("\n"),
      url: null // Would be set by GitHub API
    };
  }

  // ─── HOOKS ─────────────────────────────────────────────────────────────────

  setupHooks() {
    const hooksDir = ".git/hooks";

    // Pre-commit hook
    const preCommit = `#!/bin/sh
# CODEMASTER Pre-commit Hook
echo "🔍 Running pre-commit checks..."
npm run lint --if-present
npm test --if-present -- --passWithNoTests
`;

    // Commit-msg hook
    const commitMsg = `#!/bin/sh
# CODEMASTER Commit Message Hook
MSG=$(cat "$1")
if ! echo "$MSG" | grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\\(.+\\))?: .+"; then
  echo "❌ Invalid commit message format"
  echo "Use: type(scope): description"
  exit 1
fi
`;

    return {
      preCommit,
      commitMsg,
      hooksDir
    };
  }

  // ─── UTILITIES ─────────────────────────────────────────────────────────────

  isRepo() {
    return this.execSafe("git rev-parse --is-inside-work-tree") === "true";
  }

  init() {
    if (this.isRepo()) {
      return { initialized: false, message: "Already a git repository" };
    }

    this.exec("git init");
    return { initialized: true, message: "Repository initialized" };
  }

  clean(options = {}) {
    const { dryRun = true, directories = false, force = false } = options;

    let cmd = "git clean";
    if (dryRun) cmd += " -n";
    if (force && !dryRun) cmd += " -f";
    if (directories) cmd += " -d";

    return this.exec(cmd);
  }

  blame(file) {
    return this.exec(`git blame "${file}"`);
  }

  log(options = {}) {
    const { count = 20, oneline = true, graph = false } = options;

    let cmd = `git log -${count}`;
    if (oneline) cmd += " --oneline";
    if (graph) cmd += " --graph";

    return this.exec(cmd);
  }
}

export default GitAutomation;
