#!/bin/bash
# a script to get status code of a request
curl -sL -w "%{http_code}" "$1" -o /dev/null
