#!/usr/bin/python3

'''send request ti URL and display body of response decoded in utf-8'''
if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
