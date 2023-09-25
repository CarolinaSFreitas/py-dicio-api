url_api = "http://localhost:3000/"

import requests

response = requests.get(url_api+"marcas")

marcas = response.json

print(marcas)

