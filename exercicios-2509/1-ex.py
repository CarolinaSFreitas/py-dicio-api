# 1) INCLUIR VINHOS - não esquecer que: precisa primeiro registrar a marca antes de registrar o vinho
url_api = "http://localhost:3000/vinhos"
import requests
vinhos = {"tipo": "Suave", "marca_id": 2, "preco": 16.49, "teor": 9.0}
response = requests.post(url_api, json=vinhos)
print(response.json())
