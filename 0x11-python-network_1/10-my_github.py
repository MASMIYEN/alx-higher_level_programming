#!/usr/bin/python3
"""
This script uses the GitHub API to display a GitHub ID based on given credentials.
It takes two command line arguments: the GitHub username and the GitHub token.
It uses a bearer token for authentication.
"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
        exit()
    print(res.json()["id"])