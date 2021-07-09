import csv

with open("3.Aplicações/brasil_covid.csv", "r") as arquivo:
    # Criando um Leitor
    leitor = csv.reader(arquivo)
    print("Conteúdo do Arquivo:")
    header = next(leitor)
    for linha in leitor:
        # Mostrar "novos_casos" quando for maior que 0
        if float(linha[2]) > 0:
            print(linha)

print("\n Usando Somente Python")

with open("3.Aplicações/brasil_covid.csv", "r") as arquivo:
    # Ler todas as linhas
    linhas = arquivo.read()
    # Separar elas em uma lista, fazendo um split em cima do \n
    linhas = linhas.split("\n")
    # Para cada linha fazer um split na "," que é o valor que separa os dados
    for linha in linhas:
        linha = linha.split(",")
        print(linha)
