#!/usr/bin/python3

'''
script that takes your Github credentials (username and password)
and uses the Github API to display your id
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
