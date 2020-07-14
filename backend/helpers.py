import requests
import os
import subprocess
from backend.settings import Config
from typing import Dict, Callable

__all__ = ["update_database", "retrieve_data"]


def update_database(database=Config.DATABASE, method=""):
    if not os.path.isfile(database):
        open(database, "a").close()
    subprocess.run(["gtfs2db", "overwrite", Config.ZIPFILE, f"{database}"])


def extract_dpp() -> Dict[str, str]:
    """Fetch filename and url for specific scenario"""
    with requests.get(Config.RESOURCE_URL) as request:
        file_url = request.json()["result"]["resources"][0]["url"]
        filename = file_url.split("/")[-1]
        return {"file_url": file_url, "filename": filename}


def save(filename: str, file_url: str, chunk_size: int = 1024) -> None:
    """save retrieved file to specified location"""
    path = os.path.join(Config.RESOURCE_DIR, filename)
    if not os.path.exists(Config.RESOURCE_DIR):
        os.makedirs(Config.RESOURCE_DIR)

    with requests.get(file_url) as zipfile:
        with open(path, "wb") as f:
            for chunk in zipfile.iter_content(chunk # noqa: 
    """process"""
    data = method()
    filename, file_url = data["filename"], data["file_url"]
    save(filename, file_url)


if __name__ == "__main__":
    retrieve_data()
