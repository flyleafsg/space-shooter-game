# Simple JSON persistence for high score and last level played

import json
import os
from settings import DATA_FILE

def load_progress():
    if not os.path.exists(DATA_FILE):
        return {"high_score": 0, "max_level": 1}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_progress(high_score, max_level):
    with open(DATA_FILE, 'w') as f:
        json.dump({"high_score": high_score, "max_level": max_level}, f)
