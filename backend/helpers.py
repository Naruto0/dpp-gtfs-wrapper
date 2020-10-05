import requests
import os
import subprocess
from typing import Dict, Callable

from backend.checks import run_check
from backend.settings import Config
from backend.hash_api import check_hash_same, save_hash_to_file

__all__ = ["update_database", "retrieve_data"]


def update_database(database=Config.DATABASE, method=""):
    if not os.path.isfile(database):
        open(database, "a").close()
    subprocess.run(["gtfs2db", "overwrite", Config.ZIPFILE, f"{database}"])


def extract_dpp() -> Dict[str, str]:
    """Fetch filename, url and hash for specific scenario"""
    with requests.get(Config.RESOURCE_URL) as request:
        data = request.json()["result"]["resources"][0]
        file_url = data["url"]
        file_hash = data["hash"]
        filename = file_url.split("/")[-1]
        return {
            "file_url": file_url,
            "filename": filename,
            "file_hash": file_hash
        }


def save(
    filename: str,
    file_url: str,
    sha: str,
    chunk_size: int = 1024
) -> None:
    """save retrieved file to specified location"""
    path: str = os.path.join(Config.RESOURCE_DIR, filename)
    if not os.path.exists(Config.RESOURCE_DIR):
        os.makedirs(Config.RESOURCE_DIR)

    with requests.get(file_url) as zipfile:
        with open(path, "wb") as f:
            for chunk in zipfile.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    save_hash_to_file(sha)


def retrieve_data(method: Callable = extract_dpp):
    """process"""
    data: dict = method()
    filename, file_url, file_hash = (
        data["filename"],
        data["file_url"],
        data["file_hash"],
    )
    if check_hash_same(file_hash):
        pass
    else:
        save(filename, file_url, file_hash)
        run_check()
        update_database()


if __name__ == "__main__":
    retrieve_data()
