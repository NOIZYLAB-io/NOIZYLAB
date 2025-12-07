"""
GitControl Usage Examples
"""

from gitcontrol import GitControl, GitControlConfig, GitControlError


def setup_configuration():
    """Example: Setting up GitControl configuration"""
    print("=== Configuration Setup ===")
    
    config = GitControlConfig()
    
    # Set authentication tokens
    config.set_token("github", "your_github_token_here")
    config.set_token("gitlab", "your_gitlab_token_here")
    
    # Add directories to search for repositories
    config.add_git_directory("/home/user/projects")
    config.add_git_directory("/home/user/work")
    
    # Set user information
    config.set_user_info("github", "your_username", "your@email.com")
    
    print("✅ Configuration set up successfully!")


def list_repositories_example():
    """Example: List all git repositories"""
    print("\n=== List Repositories ===")
    
    gc = GitControl()
    
    # List all repositories in configured directories
    repos = gc.list_git_repositories()
    
    print(f"Found {len(repos)} repositories:")
    for repo in repos:
        print(f"  📁 {repo['name']}")
        print(f"     Path: {repo['path']}")
        print(f"     Branch: {repo['branch']}")
        print(f"     Status: {repo['status']}")
        print(f"     Remote: {repo['remote']}")
        print()


def clone_repository_example():
    """Example: Clone repositories"""
    print("\n=== Clone Repository ===")
    
    gc = GitControl()
    
    # Clone a public repository
    success = gc.clone_repository(
        repo_url="https://github.com/octocat/Hello-World.git",
        destination="./hello-world-clone",
        branch="master"
    )
    
    if success:
        print("✅ Repository cloned successfully!")
    else:
        print("❌ Failed to clone repository")


def repository_status_example():
    """Example: Get repository status"""
    print("\n=== Repository Status ===")
    
    gc = GitControl()
    
    try:
        # Get status of current directory (assuming it's a git repo)
        status = gc.get_repository_status(".")
        
        print("Repository Status:")
        print(f"  Current Branch: {status['current_branch']}")
        print(f"  Tracking Branch: {status.get('tracking_branch', 'None')}")
        print(f"  Has Changes: {status['has_changes']}")
        print(f"  Commits Ahead: {status.get('commits_ahead', 0)}")
        print(f"  Commits Behind: {status.get('commits_behind', 0)}")
        
        if status['changes']:
            print("  Changed Files:")
            for change in status['changes']:
                print(f"    {change}")
                
    except GitControlError as e:
        print(f"❌ Error: {e}")


def create_pull_request_example():
    """Example: Create a pull request"""
    print("\n=== Create Pull Request ===")
    
    gc = GitControl()
    
    try:
        success = gc.create_pull_request(
            repo_path=".",  # Current directory
            title="Fix critical bug in authentication",
            body="This PR addresses the authentication issue found in production. Changes include:\n- Fixed token validation\n- Added error handling\n- Updated tests",
            base_branch="main",
            head_branch="bugfix-auth"
        )
        
        if success:
            print("✅ Pull request created successfully!")
        else:
            print("❌ Failed to create pull request")
            
    except GitControlError as e:
        print(f"❌ Error: {e}")


def sync_repository_example():
    """Example: Sync repository with remote"""
    print("\n=== Sync Repository ===")
    
    gc = GitControl()
    
    try:
        success = gc.sync_repository(
            repo_path=".",
            auto_pull=True,
            auto_push=False
        )
        
        if success:
            print("✅ Repository synced successfully!")
        else:
            print("❌ Failed to sync repository")
            
    except GitControlError as e:
        print(f"❌ Error: {e}")


def batch_operations_example():
    """Example: Batch operations on multiple repositories"""
    print("\n=== Batch Operations ===")
    
    gc = GitControl()
    
    # Get all repositories
    repos = gc.list_git_repositories()
    
    print(f"Processing {len(repos)} repositories...")
    
    for repo in repos:
        print(f"\n📁 Processing {repo['name']}...")
        
        try:
            # Get status
            status = gc.get_repository_status(repo['path'])
            
            # Check if repo has uncommitted changes
            if status['has_changes']:
                print(f"  ⚠️  Repository has uncommitted changes")
            
            # Check if repo is behind remote
            if status.get('commits_behind', 0) > 0:
                print(f"  📥 Repository is {status['commits_behind']} commits behind")
                
                # Optionally sync
                # gc.sync_repository(repo['path'], auto_pull=True)
            
            # Check if repo is ahead of remote
            if status.get('commits_ahead', 0) > 0:
                print(f"  📤 Repository is {status['commits_ahead']} commits ahead")
            
            print(f"  ✅ {repo['name']} processed")
            
        except GitControlError as e:
            print(f"  ❌ Error processing {repo['name']}: {e}")


def search_and_filter_example():
    """Example: Search and filter repositories"""
    print("\n=== Search and Filter ===")
    
    gc = GitControl()
    
    # Get all repositories
    repos = gc.list_git_repositories()
    
    # Filter by status
    dirty_repos = [repo for repo in repos if repo['status'] == 'dirty']
    clean_repos = [repo for repo in repos if repo['status'] == 'clean']
    
    print(f"Clean repositories: {len(clean_repos)}")
    print(f"Dirty repositories: {len(dirty_repos)}")
    
    # Filter by branch
    main_branch_repos = [repo for repo in repos if repo['branch'] in ['main', 'master']]
    feature_branch_repos = [repo for repo in repos if repo['branch'].startswith('feature/')]
    
    print(f"Repositories on main/master: {len(main_branch_repos)}")
    print(f"Repositories on feature branches: {len(feature_branch_repos)}")
    
    # Filter by remote
    github_repos = [repo for repo in repos if 'github.com' in repo['remote']]
    gitlab_repos = [repo for repo in repos if 'gitlab.com' in repo['remote']]
    
    print(f"GitHub repositories: {len(github_repos)}")
    print(f"GitLab repositories: {len(gitlab_repos)}")


def main():
    """Run all examples"""
    print("GitControl Examples")
    print("==================")
    
    try:
        setup_configuration()
        list_repositories_example()
        repository_status_example()
        batch_operations_example()
        search_and_filter_example()
        
        # Uncomment these to test actual operations
        # clone_repository_example()
        # create_pull_request_example()
        # sync_repository_example()
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
