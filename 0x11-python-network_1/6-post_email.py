#!/usr/bin/python3

'''send POST request and display body of the response'''
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    load = {'email': sys.argv[2]}
    r = requests.post(url, data=load)
    print(r.text)
