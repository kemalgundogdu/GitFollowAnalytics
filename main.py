from src.services.follower_analyzer import FollowerAnalyzer

def main():
    analyzer = FollowerAnalyzer()
    
    username = input("GitHub kullanıcı adınızı girin: ")
    analyzer.analyze_and_display(username)

if __name__ == "__main__":
    main() 