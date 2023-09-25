##1) INCLUIR VINHOS - não esquecer que: precisa primeiro registrar a marca antes de registrar o vinho
import requests
api_url = "http://localhost:3000/"
vinhos = {"tipo": "Suave", "marca_id": 2, "preco": 18.49, "teor": 9.0}
response = requests.post(api_url, json=vinhos)
print(response.json())

