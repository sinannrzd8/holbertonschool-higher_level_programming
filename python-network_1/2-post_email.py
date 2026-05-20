#!/usr/bin/python3
"""Sends a POST request with an email parameter."""
import sys
from urllib import parse, request

if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    with request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode('utf-8'))
