#!/bin/bash
# Displays only the HTTP status code of a request
curl -s -o /dev/null -w "%{http_code}" "$1"
