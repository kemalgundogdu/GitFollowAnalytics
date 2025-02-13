from rich.console import Console
from rich.table import Table
import webbrowser

class ConsoleManager:
    def __init__(self):
        self.console = Console()
    
    def display_results(self, non_followers):
        """Sonuçları tablo halinde gösterir"""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("No", style="dim")
        table.add_column("Kullanıcı Adı")
        table.add_column("Profil Linki")
        
        for idx, user in enumerate(non_followers, 1):
            profile_url = f"https://github.com/{user.login}"
            table.add_row(str(idx), user.login, profile_url)
        
        self.console.print("\n[bold green]Sizi takip etmeyen kullanıcılar:[/bold green]")
        self.console.print(table)
        
        self.handle_user_interaction(list(non_followers))
    
    def handle_user_interaction(self, non_followers):
        """Kullanıcı etkileşimlerini yönetir"""
        while True:
            choice = input("\nProfil açmak için kullanıcı numarasını girin (çıkmak için 'q'): ")
            if choice.lower() == 'q':
                break
            
            try:
                idx = int(choice) - 1
                user = non_followers[idx]
                webbrowser.open(f"https://github.com/{user.login}")
            except (ValueError, IndexError):
                self.console.print("[bold red]Geçersiz seçim! Lütfen tekrar deneyin.[/bold red]") 