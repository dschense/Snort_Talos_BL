import requests
import os
from git import Repo

# Konfiguration
url = "https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/034/750/original/ip-filter.blf"
local_file_path = "/tmp/ip-filter.blf"
repo_path = "/path/to/your/github/repo"
commit_message = "Automated update of IP blocklist"

# 1. Datei herunterladen
response = requests.get(url)
if response.status_code == 200:
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print("Datei erfolgreich heruntergeladen!")
else:
    print(f"Fehler beim Abrufen der Datei: {response.status_code}")
    exit(1)

# 2. Datei ins Repository einfügen
repo = Repo(repo_path)
repo.git.add(local_file_path)
repo.index.commit(commit_message)
origin = repo.remote(name="origin")
origin.push()
print("Datei erfolgreich nach GitHub gepusht!")
