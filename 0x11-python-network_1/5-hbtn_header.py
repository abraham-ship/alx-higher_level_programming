#!/usr/bin/python3

'''send request to URL and display value of X-Request-Id in the response'''
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
