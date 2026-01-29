import json
import os
from config import FILENAME, FILENAME_HIGHEST



def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}  
    
def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def load_highest_id():
    if os.path.exists(FILENAME_HIGHEST):
        with open(FILENAME_HIGHEST, "r") as f:
            return json.load(f)
    return 0
def save_highest_id(id):
    with open(FILENAME_HIGHEST, "w") as f:
        json.dump(id, f, indent=1)