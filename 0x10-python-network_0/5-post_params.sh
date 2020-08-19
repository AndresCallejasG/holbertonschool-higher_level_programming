#!/bin/bash
# sends a POST request to the passed URL. Variable email and subject. Displays the body of the response
curl -sL -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
