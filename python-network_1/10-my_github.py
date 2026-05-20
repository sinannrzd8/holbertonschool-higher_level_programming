#!/usr/bin/python3
"""GitHub API authentication to get user id."""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
