import requests

url_vinhos = "http://localhost:3000/vinhos"
response= requests.get(url_vinhos)
vinhos = response.json()
print(response.json())
