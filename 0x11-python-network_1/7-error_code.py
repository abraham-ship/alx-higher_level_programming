#!/usr/bin/python3

'''send request to URL and display body of the response'''
if __name__ == '__main__':
    import requests
    import sys
    from requests.exceptions import HTTPError
    try:
        url = sys.argv[1]
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {response.status_code}")
