#3) Listar marcas e vinhos (nome da marca e dados do vinho)
import requests

url_marcas = "http://localhost:3000/marcas"
response_marcas = requests.get(url_marcas)
marcas = response_marcas.json()

url_vinhos = "http://localhost:3000/vinhos"
response_vinhos = requests.get(url_vinhos)
vinhos = response_vinhos.json()

for marca in marcas:
    print(f"Marca: {marca['nome']} - Vinhos: {marca['Vinhos']}")
    

