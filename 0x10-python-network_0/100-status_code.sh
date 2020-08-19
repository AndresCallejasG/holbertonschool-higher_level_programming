#!/bin/bash
# sends a POST request to the passed URL. Variable email and subject. Displays the body of the response
curl -sI -o /dev/null-X POST -w "%{http_code}" "$1" 
