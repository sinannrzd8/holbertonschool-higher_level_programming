#!/bin/bash
# Displays the size of the response body in bytes
curl -s "$1" | wc -c
