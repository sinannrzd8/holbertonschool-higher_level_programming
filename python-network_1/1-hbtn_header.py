#!/usr/bin/python3
"""Fetches X-Request-Id from response headers."""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
