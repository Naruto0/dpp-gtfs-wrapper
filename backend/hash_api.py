import hashlib
import pickle
import os
import logging

from typing import IO

HASH_FILE = "resources/.last-hash"

if not os.path.exists(HASH_FILE):
    f: IO = open(HASH_FILE, "a")
    f.close()


def read_hash_from_file() -> dict:
    data: dict = {}
    try:
        with open(HASH_FILE, "rb") as rf:
            data = pickle.load(rf)
    except EOFError as e:
        logging.error("Hash file is empty!")
        data["last_hash"] = None
    return data


def save_hash_to_file(sha: str):
    with open(HASH_FILE, "wb") as sf:
        pickle.dump({"last_hash": sha}, sf)


def check_hash_same(new_hash: str):
    old_hash: str = read_hash_from_file()["last_hash"]
    return old_hash == new_hash
