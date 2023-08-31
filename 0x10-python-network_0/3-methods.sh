#!/bin/bash
# a script to show methods that a server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
