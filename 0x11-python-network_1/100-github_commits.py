#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits?per_page=10"
    response = requests.get(url)

    commits = response.json()
    for commit in commits:
        print(f"{commit.get('sha')}: {commit.get('commit').get('author').get('name')}")