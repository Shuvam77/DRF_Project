from lib2to3.pgen2 import token
import requests
from getpass import getpass



auth_endpoint = "http://127.0.0.1:8000/api/auth/"

username = input("What is your username?\n");
password = getpass("What is your password?\n")

get_auth_response = requests.post(auth_endpoint, json={'username': username, 'password':password})


print(get_auth_response.json())
# print(get_auth_response.status_code)

if get_auth_response.status_code == 200:
    token = get_auth_response.json()['token']
    headers = {
        # "Authorization": f"Token {token}"
        #insted of token autherize as bearer
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
    print(get_response.status_code)


