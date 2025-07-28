import json
import os

HISTORY_FILE = "history.json"

def save_translation(original: str, translated: str, language: str = "Urdu"):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                pass

    history.append({
        "original": original,
        "translated": translated,
        "language": language
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
