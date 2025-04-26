
# logger.py
import json
import os
import logging
from settings import DATA_FILE

# Configure logging to file
logging.basicConfig(
    filename="game.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


def load_progress():
    if not os.path.exists(DATA_FILE):
        return {"high_score": 0, "max_level": 1}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_progress(high_score, max_level):
    with open(DATA_FILE, "w") as f:
        json.dump({"high_score": high_score, "max_level": max_level}, f)
    logging.info(f"Progress saved: high_score={high_score}, max_level={max_level}")


def log_event(event):
    logging.info(event)

