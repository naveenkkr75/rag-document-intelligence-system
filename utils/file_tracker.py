import json
import hashlib
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# metadata/indexed_files.json
TRACKER_FILE = BASE_DIR / "metadata" / "indexed_files.json"

# Create metadata folder if needed
TRACKER_FILE.parent.mkdir(exist_ok=True)

# Create JSON file if it doesn't exist
if not TRACKER_FILE.exists():
    TRACKER_FILE.write_text("[]")


def get_file_hash(file_path):
    sha = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha.update(chunk)

    return sha.hexdigest()


def load_hashes():
    with open(TRACKER_FILE, "r") as f:
        return json.load(f)


def save_hashes(hashes):
    with open(TRACKER_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def is_indexed(file_path):
    file_hash = get_file_hash(file_path)
    return file_hash in load_hashes()


def add_file(file_path):
    hashes = load_hashes()

    file_hash = get_file_hash(file_path)

    if file_hash not in hashes:
        hashes.append(file_hash)
        save_hashes(hashes)