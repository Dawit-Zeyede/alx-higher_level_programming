#!/bin/bash
# request the passed URL using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
