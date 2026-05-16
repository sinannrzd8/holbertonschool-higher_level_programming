#!/bin/bash
# Sends a POST request with email and subject parameters
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
