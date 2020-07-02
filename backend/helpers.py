import requests

from backend.settings import Config


def fetch_dpp():
    with requests.get(Config.RESOURCE_URL) as req:
        file_url = req.json()['result']['resources'][0]['url']
        filename = file_url.split('/')[-1]
        save(filename, file_url)

def save(filename, file_url):
    path = filename
    with requests.get(file_url) as zipfile:
        with open(path,'wb') as f:
            f.write(zipfile)