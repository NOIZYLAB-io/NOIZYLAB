# Repo Maintenance Worker

This contains a scheduled GitHub Actions workflow and a script to help maintain remote branches and run a local git gc in the Actions runner.

Default behavior:
- Runs weekly (configurable in .github/workflows/maintenance.yml).
- Dry-run mode by default (no deletions). To actually delete branches, run the workflow with workflow_dispatch and set execute=true.
- Identifies branches that are merged into the default branch OR have last commit older than KEEP_DAYS (default 30).
- Never deletes protected branches or the repository default branch.

Configuration (via workflow dispatch inputs or editing the workflow):
- execute: 'true' to actually delete candidate branches (default: 'false').
- keep_days: branches with last commit newer than this are kept (default: 30).
- protected_branches: comma-separated list of extra branch names to protect.
- allow_prune: whether to run git remote prune and git gc (default: true).

Safety notes:
- The workflow uses GITHUB_TOKEN to authenticate and delete branches. Branch protection rules are enforced by GitHub.
- This does NOT rewrite history or remove large files from the remote. For history rewrites you must intentionally run a different process and coordinate with collaborators.
- Test in a sandbox repository / run as dry-run before enabling execute=true.

Defaults I will use for the PR unless you tell me otherwise:
- Branch name: maintenance/cleanup-worker
- PR title: Add scheduled repo maintenance workflow
- schedule: weekly, Sunday 03:00 UTC
- keep_days: 30
- protected_branches: main,master
- execute (dry-run): false
- allow_prune: true

Please create a branch named maintenance/cleanup-worker and open a PR with these three files added at the specified paths. Keep the workflow in dry-run (execute=false) by default. Please add a brief PR description explaining the safety defaults and how to enable deletions via workflow_dispatch.
