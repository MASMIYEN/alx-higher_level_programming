#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    # Check if the user provided enough command line arguments
    if len(sys.argv) < 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
        sys.exit(1)

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits?per_page=10"

    # Send the GET request
    response = requests.get(url)

    try:
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Get the list of commits
        commits = response.json()

        # Print the SHA and author name for each commit
        for commit in commits:
            print(f"{commit.get('sha')}: {commit.get('commit').get('author').get('name')}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
