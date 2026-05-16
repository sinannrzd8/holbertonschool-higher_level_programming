#!/bin/bash
# Makes a request that triggers "You find me!"
curl -sL -X PUT -H "User-Agent: You got me!" 0.0.0.0:5000/catch_me
