#!/bin/bash
# GET request to the URL. Header var X-HolbertonSchool-User-Id:98. Displays the body of the response
curl -sL -X GET -H "X-HolbertonSchool-User-Id:98" "$1"
