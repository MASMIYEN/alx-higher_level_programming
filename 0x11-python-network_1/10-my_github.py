#!/usr/bin/python3
"""
This script uses the GitHub API to display a GitHub ID based on given credentials.
It takes two command line arguments: the GitHub username and the GitHub token.
It uses a bearer token for authentication.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get("https://api.github.com/user", headers=headers)

    if response.status_code >= 400:
        print("None")
    else:
        print(response.json().get("id"))
