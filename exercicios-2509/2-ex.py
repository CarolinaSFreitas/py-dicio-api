# -------------------------------------------------------------------------------------------------------------------
### 2) LISTAR AS MARCAS DE VINHO 

url_api = "http://localhost:3000/"

import requests

response = requests.get(url_api+"marcas")
marcas = response.json()
#print(marcas) retorno

# -------------------------------------------------------------------------------------------------------------------
## 2) PERCORRE AS MARCAS E RETORNA EM FORMATO DE DICIONÁRIO, TAMBÉM CONTA QUANTOS VINHOS TEM DAS MARCAS REGISTRADAS 

for marca in marcas:
    print(f"{marca['nome']} - {marca['cidade']} - {len(marca['Vinhos'])} vinhos") #mostra QUANTOS vinhos tem da marca

