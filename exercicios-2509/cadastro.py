import requests
url_api = "http://localhost:3000/"

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*len(texto))

##INCLUIR 
def incluir():
    titulo("Inclusão de Dados")

    tipo = input("Tipo do Vinho: ")
    marca_id = input("Código da Marca: ")
    teor = float(input("Teor Alcoólico: "))
    preco = input("Preço do Vinho R$........: ")

    dic_vinho = {"tipo": tipo, "marca_id": marca_id, "teor": teor, "preco": preco}

    response = requests.post(url_api+"vinhos", json=dic_vinho)
    
    if response.status_code == 201:
        vinho = response.json()
        print(f"Ok! Vinho cadastrado com o código: {vinho['id']}")
    else:
        print("Erro... Não cadastrado.")

##LISTAR MARCAS EM ORDEM (NOME, CIDADE E Nº DE VINHOS)
def listar_marcas_ordem():
    pass

while True:
    titulo("Cadastro de Vinhos", "=")
    print("1. Incluir vinhos")
    print("2. Listar marcas em ordem (nome, cidade e nº de vinhos)")
    print("3. Listar marcas e vinhos (nome da marca e dados do vinho)")
    print("4. Listar vinhos (tipo, nome da marca, teor e preço)")
    print("5. Estatística de vinhos (número, preço médio, +caro e +barato)")
    print("6. Pesquisa por tipo")
    print("7. Pesquisa por intervalo de preços")
    print("8. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar_marcas_ordem()
    else:
        break