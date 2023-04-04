#!/bin/bash
 bash script that takes in a url and displays size of the body of the response
curl -s -H GET "$1" | wc -c
