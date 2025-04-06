import json
from typing import Any

def get_web_url() -> str:
    """
    Retrieves the website URL from 'config.json'.
    """
    with open("config.json", 'r', encoding='utf-8') as file:
        config: dict[str, Any] = json.load(file)
    return config["config_path"]["web_url"]
