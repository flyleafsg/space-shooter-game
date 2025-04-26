
import json, os, logging
from settings import DATA_FILE

logging.basicConfig(
    filename="game.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

def load_progress():
    if not os.path.exists(DATA_FILE):
        return {"high_score": 0, "max_level": 1}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        # File is empty or corrupted
        return {"high_score": 0, "max_level": 1}

def save_progress(high_score, max_level):
    # … your existing save logic …
