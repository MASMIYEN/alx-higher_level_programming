#!/usr/bin/python3
"""
This script uses the GitHub API to display a GitHub ID based on given credentials.
It takes two command line arguments: the GitHub username and the GitHub token.
It uses a bearer token for authentication.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {password}"}

    r = requests.get(
        url,
        headers=headers,
    )
    print(r.json().get("id"))
