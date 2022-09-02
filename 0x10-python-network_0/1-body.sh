#!/bin/bash
#Bash script that takes in a URL, and displays the body of the response
curl -sL -X GET "$1"
