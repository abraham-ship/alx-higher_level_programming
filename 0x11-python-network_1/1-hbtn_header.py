#!/usr/bin/python3

'''send request to url and display value of X-Request-Id in header'''
if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers["X-Request-Id"])
