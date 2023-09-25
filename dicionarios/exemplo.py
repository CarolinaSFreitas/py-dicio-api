# AULA 1 SOBRE DICIONÁRIOS EM PYTHON - 18/09

# as listas / vetores / arrays são representadas assim:
produtos = []

# tuplas 
# são de certa forma semelhantes as listas, porém as tuplas são "IMUTÁVEIS"
alunos = (12, 20)

#-----------------------------------------------------------------------------------------#

# DICIONÁRIOS / objetos (no javascript)
agendas = {} # forma mais usual
agendas = dict()

# exemplos de dicionários: 

print('EXEMPLOS DE DICIONÁRIOS - CONTATOS\n')


contatos = {"Ana": "984524178", 
            "Bianca": "981145270", 
            "Ursula": "99954121360",
            "Romário": "984120358"}
              #chave      #valor

#-----------------------------------------------------------------------------------------#

    #formas de alterar o conteúdo do dicionário
contatos["Zé"] = "3252-9841"
contatos.update({"Eduardo": "9998410247"})

#-----------------------------------------------------------------------------------------#

    # formas de imprimir os dicionários
print(contatos) # como imprimir esse dicionário de contatos

print('-----------------------------------------------------------------------------------------')

print(contatos["Romário"]) # imprimindo o valor associonado buscando pela chave "nome"

print('-----------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------------------------#

    #FORMAS DE PERCORRER O DICIONÁRIO
# Esse loop for irá retornar/percorrer as chaves do dicionário ("keys")
for nome in contatos.keys():
    print(nome)

print('-----------------------------------------------------------------------------------------')

# Esse loop for irá retornar/percorrer os valores do dicionário ("values")
for fone in contatos.values():
    print(fone)

print('-----------------------------------------------------------------------------------------')


# Esse loop for irá retornar/percorrer as chaves e os valores do dicionário ("items")
for (nome, fone) in contatos.items():
    print(f"{nome} - {fone}")

print('-----------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------------------------#

    #PRINCIPAL APLICAÇÃO: LISTAS DE DICIONÁRIOS

print('EXEMPLOS DE APLICAÇÃO: LISTAS DE DICIONÁRIOS\n')

clientes = [{"nome": "Luis Carlos", "idade": 25},
           {"nome": "Maria Julia", "idade": 29},
           {"nome": "Antonieta Machado", "idade": 30},
           {"nome": "Cleide Candida", "idade": 22},
           {"nome": "Josué Martins", "idade": 35},
           {"nome": "Gabriel Matias", "idade": 23},
           {"nome": "Judas de Jesus", "idade": 39},
           {"nome": "Capri da Silva", "idade": 26}
]

#listar os dados
for cliente in clientes:
    print(f"{cliente['nome']} - {cliente['idade']} anos")

print('-----------------------------------------------------------------------------------------')

# ordenar os elementos da lista POR ORDEM ALFABETICA DE NOME
# Lambda: palavra reservada do Python p/ declarar uma função anonima. 
clientes2 = sorted(clientes, key = lambda cliente: cliente ["nome"])

for cliente in clientes2:
    print(f"{cliente['nome']} - {cliente['idade']} anos")

print('-----------------------------------------------------------------------------------------')    

# ordenar os elementos da lista POR ORDEM DE IDADE
# Lambda: palavra reservada do Python p/ declarar uma função anonima. 
clientes3 = sorted(clientes, key = lambda cliente: cliente ["idade"])

for cliente in clientes3:
    print(f"{cliente['nome']} - {cliente['idade']} anos")

print('-----------------------------------------------------------------------------------------')    

print('IMPORTANDO CSV\n')

import csv

with open('clientes.csv', mode='w') as arquivo:
    colunas = ["nome", "idade"]
    writer = csv.DictWriter(arquivo, fieldnames=colunas)

    writer.writeheader()
    for cliente in clientes2:
        writer.writerow(cliente)