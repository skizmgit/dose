import json
import os
from pathlib import Path

from common import calc
from model.dosebook import DoseBook

DOSEBOOKS_PATH = Path('dosebooks')

def write_dosebook(dosebook: DoseBook, filename):
    """Writes a dosebook to a JSON file in the dosebooks directory."""
    ensure_dosebook_dir_exists()
    file_path = DOSEBOOKS_PATH / filename
    with file_path.open('w') as file:
        json.dump(dosebook.to_dict(), file, indent=4)
    print(f"dosebook saved to {file_path}")

def read_dosebook(filename):
    """Read dosebook from a JSON file in the dosebooks directory."""
    file_path = DOSEBOOKS_PATH / filename
    if file_path.exists():
        with file_path.open('r') as file:
            dosebook = DoseBook.from_dict(json.load(file))
        return dosebook
    else:
        print(f"{file_path} not found.")
        return None

def delete_dosebook(filename):
    """Deletes a dosebook from the dosebooks directory"""
    file_path = f"{DOSEBOOKS_PATH}/{filename}"
    try:
        os.remove(file_path)
        print(f"File {file_path} has been deleted successfully.")
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except PermissionError:
        print(f"You do not have permission to delete {file_path}.")
    except Exception as e:
        print(f"Error: {e}")

def is_dosebook_empty(dosebook):
    return dosebook is None or not dosebook
def clear_dosebook(dosebook):
    """Resets working dosebook"""
    dosebook = None

def list_dosebooks():
    """Lists all the saved dosebooks in the dosebooks directory"""
    ensure_dosebook_dir_exists()
    dosebook_files = [f for f in os.listdir(DOSEBOOKS_PATH)
                      if os.path.isfile(os.path.join(DOSEBOOKS_PATH, f))]
    dosebook_names = [os.path.splitext(f)[0] for f in dosebook_files]
    if dosebook_names:
        for dosebook_name in dosebook_names:
            print(dosebook_name)
    else:
        print("no dosebooks found.")

def ensure_dosebook_dir_exists():
    """Ensure the dosebooks directory exists."""
    DOSEBOOKS_PATH.mkdir(exist_ok=True)

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_float(s: str) -> float:
    while not is_number(s):
        s = input(f"{s} is not a valid number.\n"
                  f">>: ")
    return float(s)

def print_taken(dosebook: DoseBook):
    print(f"{calc.taken(dosebook)} taken")

def print_remaining(dosebook: DoseBook):
    print(f"you have {calc.remaining(dosebook)} remaining")

def print_line_banner():
    print(('~' * 36) + ' dose v1 ' + ('~' * 36))

def is_db_found():
    if os.path.isdir(DOSEBOOKS_PATH):
        for item in os.listdir(DOSEBOOKS_PATH):
            full_path = os.path.join(DOSEBOOKS_PATH, item)
            if os.path.isfile(full_path) and item.endswith('.db'):
                return True
        return False
    else:
        return False