#!/bin/bash
# Makes a request that makes the server return "You find me!"
curl -sL -X PUT -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
