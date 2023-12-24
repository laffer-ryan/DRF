import requests

endpoint = "http://127.0.0.1:8000/api/products/2/update/"

data = {
    'title': 'A brand new title',
    'price': 19.95
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
