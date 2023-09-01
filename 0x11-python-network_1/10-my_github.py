#!/usr/bin/python3

'''
script that takes your Github credentials (username and password)
and uses the Github API to display your id
'''
if __name__ == "__main__":
    import requests
    from sys import argv

    usr = argv[1]
    pwd = argv[2]
    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=(usr, pwd))
        user_data = response.json()
        print(user_date["id"])
    except Exception:
        print("None")
