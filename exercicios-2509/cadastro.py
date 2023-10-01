import requests
url_api = "http://localhost:3000/"

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*len(texto))

##(1) INCLUIR 
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

##(2) LISTAR MARCAS EM ORDEM (NOME, CIDADE E Nº DE VINHOS) 
def listar_marcas_ordem():
    titulo("Listar Marcas em Ordem (nome, cidade e nº de vinhos)")

    url_api = "http://localhost:3000/marcas"
    response = requests.get(url_api)

    if response.status_code == 200:
        marcas = response.json()

        for marca in marcas:
            print(f"{marca['nome']} - {marca['cidade']} - {len(marca['Vinhos'])} vinhos")
    else:
        print("Erro ao obter a lista de marcas.")


###(3) LISTAR MARCAS E VINHOS (nome da marca e dados do vinho)
def listar_marcas_e_vinhos():
    titulo("Listar Marcas e Vinhos (nome da marca e dados do vinho)")

    ##chamada get na rota /marcas p receber as marcas
    url_marcas = "http://localhost:3000/marcas"
    response_marcas = requests.get(url_marcas)

    if response_marcas.status_code != 200:
        print("Erro ao obter a lista de marcas.")
        return

    marcas = response_marcas.json()
    ##pra cada marca, os respectivos vinhos
    for marca in marcas:
        marca_id = marca['id']
        url_vinhos_marca = f"http://localhost:3000/vinhos/por-marca/{marca_id}"
        response_vinhos_marca = requests.get(url_vinhos_marca)

        if response_vinhos_marca.status_code == 200:
            vinhos = response_vinhos_marca.json()
            print(f"Marca: {marca['nome']}")
            
            for vinho in vinhos:
                print(f"  - Tipo: {vinho['tipo']}, Preço: R${vinho['preco']}, Teor: {vinho['teor']}")
        else:
            print(f"Erro ao obter vinhos para a marca {marca['nome']}.")


# LOOP WHILE DO SISTEMA QUE CONSOME A API VINICOLA
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
    elif opcao == 3:
        listar_marcas_e_vinhos()           # ir adicionando as funções no loop
    else:
        break

