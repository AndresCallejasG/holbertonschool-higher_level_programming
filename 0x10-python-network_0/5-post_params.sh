#!/bin/bash
# GET request to the URL. Header var X-HolbertonSchool-User-Id:98. Displays the body of the response
curl -sL -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
