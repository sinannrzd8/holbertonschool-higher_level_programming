#!/usr/bin/python3
import sys
from urllib import request

with request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
