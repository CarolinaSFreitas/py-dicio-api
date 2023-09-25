#2) Listar marcas em ordem (nome, cidade e nº de vinhos)
import requests
#faz o get p/ obter as marcas de vinho
url_api = "http://localhost:3000/marcas"
response = requests.get(url_api)
marcas = response.json()

#percorre as marcas e retorna marca, cidade e o nº de vinhos
for marca in marcas:
    print(f"{marca['nome']} - {marca['cidade']} - {len(marca['Vinhos'])} vinhos")
