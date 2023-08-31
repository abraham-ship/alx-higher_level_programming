#!/bin/bash
# a script to send request to given URL and display size of body response
curl -sI "$1" | wc -c
