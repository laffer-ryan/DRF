import requests

endpoint = "http://localhost:8000/api/products/"

list_request = requests.get(endpoint)
print(list_request.json())