#!/bin/bash
# script takes in an url and displays size of the body of the response
curl -s -H GET "$1" | wc -c
