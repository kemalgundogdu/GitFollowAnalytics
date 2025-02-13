from src.api.github_client import GitHubClient
from src.utils.console import ConsoleManager

class FollowerAnalyzer:
    def __init__(self):
        self.github_client = GitHubClient()
        self.console = ConsoleManager()
    
    def get_non_followers(self, username):
        """Kullanıcıyı takip etmeyenleri bulur"""
        user = self.github_client.get_user(username)
        
        followers = set(user.get_followers())
        following = set(user.get_following())
        
        return following - followers
    
    def analyze_and_display(self, username):
        """Analiz yapar ve sonuçları gösterir"""
        non_followers = self.get_non_followers(username)
        self.console.display_results(non_followers) 