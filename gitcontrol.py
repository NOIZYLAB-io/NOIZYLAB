"""
Main GitControl class for managing Git operations
"""

import os
import subprocess
import requests
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from urllib.parse import urlparse

from .config import GitControlConfig


class GitControlError(Exception):
    """Custom exception for GitControl operations"""
    pass


class GitControl:
    """Main class for Git operations management"""
    
    def __init__(self, config_file: str = ".gitcontrol-config"):
        self.config = GitControlConfig(config_file)
    
    def _run_command(self, command: List[str], cwd: str = None, capture_output: bool = True) -> Tuple[int, str, str]:
        """Run a shell command and return exit code, stdout, stderr"""
        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=capture_output,
                text=True,
                shell=False
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            raise GitControlError(f"Command execution failed: {e}")
    
    def _is_git_repo(self, path: str) -> bool:
        """Check if a directory is a git repository"""
        return (Path(path) / '.git').exists()
    
    def list_git_repositories(self, search_paths: List[str] = None) -> List[Dict[str, str]]:
        """List all git repositories in specified directories"""
        if search_paths is None:
            search_paths = self.config.get_git_directories()
        
        repositories = []
        
        for search_path in search_paths:
            search_path = Path(search_path).expanduser()
            if not search_path.exists():
                continue
            
            # Search for git repositories
            for root, dirs, files in os.walk(search_path):
                if '.git' in dirs:
                    repo_path = Path(root)
                    
                    # Get repository info
                    repo_info = self._get_repo_info(str(repo_path))
                    if repo_info:
                        repositories.append(repo_info)
                    
                    # Don't search inside .git directories
                    dirs[:] = [d for d in dirs if d != '.git']
        
        return repositories
    
    def _get_repo_info(self, repo_path: str) -> Optional[Dict[str, str]]:
        """Get information about a git repository"""
        try:
            # Get current branch
            exit_code, branch, _ = self._run_command(['git', 'branch', '--show-current'], cwd=repo_path)
            current_branch = branch.strip() if exit_code == 0 else 'unknown'
            
            # Get remote URL
            exit_code, remote_url, _ = self._run_command(['git', 'remote', 'get-url', 'origin'], cwd=repo_path)
            remote = remote_url.strip() if exit_code == 0 else 'no-remote'
            
            # Get last commit
            exit_code, last_commit, _ = self._run_command(
                ['git', 'log', '-1', '--pretty=format:%h %s'], cwd=repo_path
            )
            last_commit = last_commit.strip() if exit_code == 0 else 'no-commits'
            
            # Get status
            exit_code, status, _ = self._run_command(['git', 'status', '--porcelain'], cwd=repo_path)
            is_clean = len(status.strip()) == 0 if exit_code == 0 else False
            
            return {
                'path': repo_path,
                'name': Path(repo_path).name,
                'branch': current_branch,
                'remote': remote,
                'last_commit': last_commit,
                'status': 'clean' if is_clean else 'dirty'
            }
        except Exception as e:
            print(f"Error getting repo info for {repo_path}: {e}")
            return None
    
    def clone_repository(self, repo_url: str, destination: str = None, branch: str = None, token: str = None) -> bool:
        """Clone a repository"""
        try:
            # Determine provider and get token if needed
            provider = self._get_provider_from_url(repo_url)
            if token is None and provider:
                token = self.config.get_token(provider)
            
            # Prepare clone URL with authentication if token is provided
            clone_url = self._prepare_clone_url(repo_url, token) if token else repo_url
            
            # Prepare command
            command = ['git', 'clone']
            
            if branch:
                command.extend(['--branch', branch])
            
            command.append(clone_url)
            
            if destination:
                command.append(destination)
            
            # Execute clone
            exit_code, stdout, stderr = self._run_command(command, capture_output=False)
            
            if exit_code == 0:
                print(f"Successfully cloned {repo_url}")
                return True
            else:
                print(f"Failed to clone {repo_url}: {stderr}")
                return False
                
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False
    
    def _get_provider_from_url(self, url: str) -> Optional[str]:
        """Extract provider from repository URL"""
        parsed = urlparse(url)
        
        if 'github.com' in parsed.netloc:
            return 'github'
        elif 'gitlab.com' in parsed.netloc:
            return 'gitlab'
        elif 'bitbucket.org' in parsed.netloc:
            return 'bitbucket'
        
        return None
    
    def _prepare_clone_url(self, url: str, token: str) -> str:
        """Prepare clone URL with authentication token"""
        parsed = urlparse(url)
        
        if parsed.scheme == 'https':
            # For HTTPS URLs, add token as username
            auth_url = f"https://{token}@{parsed.netloc}{parsed.path}"
            return auth_url
        
        return url
    
    def create_pull_request(self, repo_path: str, title: str, body: str = "", 
                          base_branch: str = None, head_branch: str = None) -> bool:
        """Create a pull request"""
        try:
            # Get repository remote URL
            exit_code, remote_url, _ = self._run_command(['git', 'remote', 'get-url', 'origin'], cwd=repo_path)
            if exit_code != 0:
                print("Error: Could not get remote URL")
                return False
            
            remote_url = remote_url.strip()
            provider = self._get_provider_from_url(remote_url)
            
            if not provider:
                print("Error: Unsupported git provider")
                return False
            
            # Get current branch if head_branch not specified
            if head_branch is None:
                exit_code, current_branch, _ = self._run_command(['git', 'branch', '--show-current'], cwd=repo_path)
                if exit_code != 0:
                    print("Error: Could not get current branch")
                    return False
                head_branch = current_branch.strip()
            
            # Use default branch if base_branch not specified
            if base_branch is None:
                base_branch = self.config.get_default_branch()
            
            # Create PR based on provider
            if provider == 'github':
                return self._create_github_pr(remote_url, title, body, base_branch, head_branch)
            elif provider == 'gitlab':
                return self._create_gitlab_mr(remote_url, title, body, base_branch, head_branch)
            else:
                print(f"Error: Pull request creation not implemented for {provider}")
                return False
                
        except Exception as e:
            print(f"Error creating pull request: {e}")
            return False
    
    def _create_github_pr(self, remote_url: str, title: str, body: str, 
                         base_branch: str, head_branch: str) -> bool:
        """Create GitHub pull request"""
        token = self.config.get_token('github')
        if not token:
            print("Error: GitHub token not found in config")
            return False
        
        # Extract owner and repo from URL
        owner, repo = self._parse_github_url(remote_url)
        if not owner or not repo:
            print("Error: Could not parse GitHub repository URL")
            return False
        
        # Prepare API request
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {
            'Authorization': f'token {token}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'title': title,
            'body': body,
            'head': head_branch,
            'base': base_branch
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=data)
            
            if response.status_code == 201:
                pr_data = response.json()
                print(f"Successfully created pull request: {pr_data['html_url']}")
                return True
            else:
                print(f"Error creating GitHub PR: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"Error making GitHub API request: {e}")
            return False
    
    def _create_gitlab_mr(self, remote_url: str, title: str, body: str, 
                         base_branch: str, head_branch: str) -> bool:
        """Create GitLab merge request"""
        token = self.config.get_token('gitlab')
        if not token:
            print("Error: GitLab token not found in config")
            return False
        
        # Extract project ID from URL
        project_id = self._parse_gitlab_url(remote_url)
        if not project_id:
            print("Error: Could not parse GitLab repository URL")
            return False
        
        # Prepare API request
        api_url = f"https://gitlab.com/api/v4/projects/{project_id}/merge_requests"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'source_branch': head_branch,
            'target_branch': base_branch,
            'title': title,
            'description': body
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=data)
            
            if response.status_code == 201:
                mr_data = response.json()
                print(f"Successfully created merge request: {mr_data['web_url']}")
                return True
            else:
                print(f"Error creating GitLab MR: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"Error making GitLab API request: {e}")
            return False
    
    def _parse_github_url(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        """Parse GitHub URL to extract owner and repo"""
        try:
            # Handle both HTTPS and SSH URLs
            if url.startswith('git@github.com:'):
                # SSH format: git@github.com:owner/repo.git
                path = url.split(':')[1]
            else:
                # HTTPS format: https://github.com/owner/repo.git
                parsed = urlparse(url)
                path = parsed.path.lstrip('/')
            
            # Remove .git suffix if present
            if path.endswith('.git'):
                path = path[:-4]
            
            parts = path.split('/')
            if len(parts) >= 2:
                return parts[0], parts[1]
            
            return None, None
            
        except Exception:
            return None, None
    
    def _parse_gitlab_url(self, url: str) -> Optional[str]:
        """Parse GitLab URL to extract project ID (simplified - uses project path)"""
        try:
            if url.startswith('git@gitlab.com:'):
                path = url.split(':')[1]
            else:
                parsed = urlparse(url)
                path = parsed.path.lstrip('/')
            
            if path.endswith('.git'):
                path = path[:-4]
            
            # For simplicity, return URL-encoded path as project ID
            return path.replace('/', '%2F')
            
        except Exception:
            return None
    
    def get_repository_status(self, repo_path: str) -> Dict[str, any]:
        """Get detailed status of a git repository"""
        if not self._is_git_repo(repo_path):
            raise GitControlError(f"Not a git repository: {repo_path}")
        
        status = {}
        
        try:
            # Current branch
            exit_code, branch, _ = self._run_command(['git', 'branch', '--show-current'], cwd=repo_path)
            status['current_branch'] = branch.strip() if exit_code == 0 else 'unknown'
            
            # Remote tracking
            exit_code, tracking, _ = self._run_command(
                ['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'], 
                cwd=repo_path
            )
            status['tracking_branch'] = tracking.strip() if exit_code == 0 else None
            
            # Uncommitted changes
            exit_code, changes, _ = self._run_command(['git', 'status', '--porcelain'], cwd=repo_path)
            status['has_changes'] = len(changes.strip()) > 0 if exit_code == 0 else False
            status['changes'] = changes.strip().split('\n') if changes.strip() else []
            
            # Commits ahead/behind
            if status['tracking_branch']:
                exit_code, ahead_behind, _ = self._run_command(
                    ['git', 'rev-list', '--left-right', '--count', f"{status['tracking_branch']}...HEAD"],
                    cwd=repo_path
                )
                if exit_code == 0:
                    parts = ahead_behind.strip().split('\t')
                    status['commits_behind'] = int(parts[0]) if len(parts) > 0 else 0
                    status['commits_ahead'] = int(parts[1]) if len(parts) > 1 else 0
            
            return status
            
        except Exception as e:
            raise GitControlError(f"Error getting repository status: {e}")
    
    def sync_repository(self, repo_path: str, auto_pull: bool = True, auto_push: bool = False) -> bool:
        """Sync repository with remote (fetch, pull, push)"""
        if not self._is_git_repo(repo_path):
            print(f"Error: Not a git repository: {repo_path}")
            return False
        
        try:
            # Fetch latest changes
            exit_code, _, stderr = self._run_command(['git', 'fetch'], cwd=repo_path)
            if exit_code != 0:
                print(f"Error fetching: {stderr}")
                return False
            
            # Get status
            status = self.get_repository_status(repo_path)
            
            # Pull if behind and auto_pull is enabled
            if auto_pull and status.get('commits_behind', 0) > 0:
                exit_code, _, stderr = self._run_command(['git', 'pull'], cwd=repo_path)
                if exit_code != 0:
                    print(f"Error pulling: {stderr}")
                    return False
                print(f"Pulled {status['commits_behind']} commits")
            
            # Push if ahead and auto_push is enabled
            if auto_push and status.get('commits_ahead', 0) > 0:
                exit_code, _, stderr = self._run_command(['git', 'push'], cwd=repo_path)
                if exit_code != 0:
                    print(f"Error pushing: {stderr}")
                    return False
                print(f"Pushed {status['commits_ahead']} commits")
            
            return True
            
        except Exception as e:
            print(f"Error syncing repository: {e}")
            return False
