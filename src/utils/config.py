import os
from pathlib import Path
import yaml

def get_github_token():
    """GitHub token'ını environment variable'dan alır"""
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable bulunamadı!")
    return token

def load_config():
    """Config dosyasından ayarları yükler"""
    config_path = Path(__file__).parent.parent.parent / 'config' / 'config.yaml'
    with open(config_path, 'r') as file:
        return yaml.safe_load(file) 