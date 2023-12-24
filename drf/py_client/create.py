import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': 'Car',
    'content': 'New Car',
    'price': 87000.00
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)

