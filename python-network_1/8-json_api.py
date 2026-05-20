#!/usr/bin/python3
"""Search user API using POST and JSON handling."""
import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        result = response.json()
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
