#!/bin/bash
# a script to send POST request and display body of the response
curl -d "email: test@gmail.com""subject: I will always be here for PLD" -X POST "$1"
