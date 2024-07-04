#!/bin/bash
# Displays onlty the staus code of the response/
curl -s -o /dev/null -w "%{http_code}" "$1"
