#!/bin/bash
#Bash script that takes in a URL, and displays the body of the response
curl -sL -H "X-HolbertonSchool-User-Id: 98" -X GET "$1"
