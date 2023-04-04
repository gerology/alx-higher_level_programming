#!/bin/bash
# send a JSON POST request to a URL passed as the first argument, and display the body of the response
curl -s -H "Content-Type=application/json" -d "$(cat "$2")" "$1"
