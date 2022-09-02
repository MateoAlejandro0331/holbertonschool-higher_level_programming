#!/bin/bash
#Bash script that takes in a URL, and displays the body of the response
curl -sL -X POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
