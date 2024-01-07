#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Check if the user provided enough command line arguments
    if len(sys.argv) < 3:
        print("Usage: ./10-my_github.py <GitHub username> <GitHub password>")
        sys.exit(1)

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send the GET request
    response = requests.get("https://api.github.com/user", auth=auth)

    try:
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Print the user's GitHub ID
        print(response.json().get("id"))
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
