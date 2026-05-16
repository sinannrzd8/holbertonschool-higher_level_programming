#!/bin/bash
# Sends a request that makes the server respond with "You got me!"
curl -sL -X PUT -H "Origin: School" 0.0.0.0:5000/catch_me
