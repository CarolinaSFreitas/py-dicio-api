### LISTAR AS MARCAS

url_api = "http://localhost:3000/"

import requests

response = requests.get(url_api+"marcas")
marcas = response.json()
#print(marcas)

## PERCORRER AS MARCAS E RETORNAR EM FORMATO DE DICIONÁRIO 
for marca in marcas:
    print(f"{marca['nome']} - {marca['cidade']} - {len(marca['Vinhos'])} vinhos") #mostra QUANTOS vinhos tem da marca