#!/bin/bash
# display all HTTP methods that the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
