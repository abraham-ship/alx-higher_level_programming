#!/usr/bin/python3

'''
send POST request
    If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    q = "" if len(argv) == 1 else argv[1]
    load = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        rj = r.json()
        if not rj:
            print("No result")
        else:
            print(f"[{rj.get('id')}] {rj.get('name')}")
    except ValueError:
        print("Not a valid JSON")
