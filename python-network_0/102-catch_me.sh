#!/bin/bash
# Sends a request that makes the server respond "You find me!"
curl -sL -X PUT -H "X-School-User-Id: 98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
