#!/bin/bash
# script takes in an url and displays size of the body of the response
curl -s "$1" | wc -c
