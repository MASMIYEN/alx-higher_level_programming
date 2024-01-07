#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
"""
import sys
import requests

if __name__ == "__main__":
    # If no argument is provided, use an empty string
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # Send the POST request
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Try to decode the response to JSON
        json_response = response.json()

        # Check if the response is empty
        if json_response == {}:
            print("No result")
        else:
            # Use f-string formatting for a more readable output
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
