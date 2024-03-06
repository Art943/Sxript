
import json
from pathlib import Path
import shutil
import os
from header import generate_prototypes


ROOT = Path(__file__).parent

try:
    # Opening JSON file using 'with open'
    with open('data.json', 'r') as f:
        # returns JSON object as a dictionary
        data = json.load(f)

    # Iterating through the json list
    for i in data['signals']:
        print(i)

except FileNotFoundError:
    print("File not found. Please check the file path.")
except json.JSONDecodeError:
    print("Error decoding JSON. Please check if the file contains valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


TEST_DIR = Path(ROOT.parent, 'test')
SIGNALS_DIR = Path(ROOT.parent, 'lib', 'signals')

print(TEST_DIR)

try:
   # shutil.rmtree(TEST_DIR, True)
    # shutil.rmtree(SIGNALS_DIR, True)
    os.makedirs(TEST_DIR, exist_ok=True)
    os.makedirs(SIGNALS_DIR, exist_ok=True)

except:
    print("Error creating directories")
    exit(1)

generate_prototypes(data)