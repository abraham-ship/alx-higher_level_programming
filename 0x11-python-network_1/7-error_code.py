#!/usr/bin/python3

'''send request to URL and display body of the response'''
if __name__ == '__main__':
    import requests
    import sys
    from requests.exceptions import HTTPError
    try:
        url = sys.argv[1]
        r = requests.get(url)
        print(r.text)
    except HTTPError as e:
        print(f"Error code: {e}")
