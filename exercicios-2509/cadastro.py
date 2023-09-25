def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*len(texto))

def incluir():
    titulo("Inclusão de Dados")

    tipo = input("Tipo do Vinho: ")
    marca_id = input("Código da Marca: ")
    teor = float(input("Teor Alcoólico: "))
    preco = input("Preço do Vinho R$........: ")

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