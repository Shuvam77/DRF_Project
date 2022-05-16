import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"Create One Class API View4",
    # "content": "This is a test4",
    "price": 55.49
}

get_response = requests.post(endpoint, json=data)


print(get_response.json())
print(get_response.status_code)


