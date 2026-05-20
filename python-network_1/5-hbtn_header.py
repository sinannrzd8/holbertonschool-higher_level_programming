#!/usr/bin/python3
"""Displays X-Request-Id from response headers."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
