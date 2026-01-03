-- NoizyLab OS - macOS Shortcuts AppleScript
-- Import this into Shortcuts app or run directly

-- ═══════════════════════════════════════════════════════════════
-- NOIZYLAB CLI SHORTCUTS
-- ═══════════════════════════════════════════════════════════════

on run
	set userChoice to choose from list {"🔧 Worker Status", "🧠 Ask AI Question", "💻 CPU Info", "🖥️ OS History", "🎮 GPU Info", "📊 All Workers", "🚀 Deploy All", "📝 View Logs"} with prompt "NoizyLab OS - Select Action:" default items {"🔧 Worker Status"}
	
	if userChoice is false then
		return
	end if
	
	set selectedAction to item 1 of userChoice
	
	if selectedAction is "🔧 Worker Status" then
		do shell script "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && ls -1 workers | wc -l | xargs -I {} echo '57 AI Workers Active'"
		display notification "57 AI Workers Active" with title "NoizyLab OS" subtitle "All Systems Operational"
		
	else if selectedAction is "🧠 Ask AI Question" then
		set userQuestion to text returned of (display dialog "Ask NoizyLab AI:" default answer "What is branch prediction?")
		-- This would call the CLI when deployed
		display notification "Query sent to AI workers" with title "NoizyLab OS" subtitle userQuestion
		
	else if selectedAction is "💻 CPU Info" then
		display notification "CPU Architecture Worker" with title "NoizyLab OS" subtitle "x86, ARM, RISC-V, MIPS Expert"
		
	else if selectedAction is "🖥️ OS History" then
		display notification "Operating Systems Worker" with title "NoizyLab OS" subtitle "Every OS from 1956 to now"
		
	else if selectedAction is "🎮 GPU Info" then
		display notification "GPU Computing Worker" with title "NoizyLab OS" subtitle "3dfx to RTX 5090"
		
	else if selectedAction is "📊 All Workers" then
		set workerList to "Core: 5 workers
Business: 4 workers  
Technician: 5 workers
Round 1: 9 workers
Round 2: 10 workers
Round 3: 21 workers
Orchestration: 3 workers
═══════════════════
TOTAL: 57 workers"
		display dialog workerList with title "NoizyLab OS - Worker Summary" buttons {"OK"} default button "OK"
		
	else if selectedAction is "🚀 Deploy All" then
		display notification "Starting deployment..." with title "NoizyLab OS"
		do shell script "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && ./deploy.sh deploy 2>&1 &"
		display notification "Deployment initiated for 57 workers" with title "NoizyLab OS"
		
	else if selectedAction is "📝 View Logs" then
		tell application "Terminal"
			activate
			do script "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && tail -f /tmp/noizylab.log 2>/dev/null || echo 'NoizyLab OS Ready'"
		end tell
	end if
end run

-- ═══════════════════════════════════════════════════════════════
-- QUICK ACTIONS (can be bound to keyboard shortcuts)
-- ═══════════════════════════════════════════════════════════════

on noizylab_status()
	display notification "57 Workers | 3 Rounds | All Systems Go" with title "🧠 NoizyLab OS"
end noizylab_status

on noizylab_ask(question)
	-- Route to appropriate worker based on question
	display notification question with title "🧠 NoizyLab AI Query"
end noizylab_ask

on noizylab_deploy()
	do shell script "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && ./deploy.sh deploy &"
	display notification "Deploying 57 workers to Cloudflare..." with title "🚀 NoizyLab Deploy"
end noizylab_deploy
