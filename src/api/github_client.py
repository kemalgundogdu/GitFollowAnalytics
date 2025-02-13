from github import Github
from src.utils.config import get_github_token

class GitHubClient:
    def __init__(self):
        self.client = None
        self.initialize_client()
    
    def initialize_client(self):
        """GitHub API client'ını başlatır"""
        token = get_github_token()
        self.client = Github(token)
    
    def get_user(self, username):
        """Belirtilen kullanıcıyı getirir"""
        return self.client.get_user(username)
    
    def get_authenticated_user(self):
        """Token ile authenticate olmuş kullanıcıyı getirir"""
        return self.client.get_user()