import csv

header = ["nome", "sobrenome"]  # Definindo Header
dados = []  # Lista vazia que vai guardar os nomes e sobrenomes
opt = input("0 que deseja fazer?\n1 - Cadastrar\n0 - Sair\n")
while opt != "0":
    nome = input("Qual seu nome? \n")
    sobrenome = input("\nQual seu sobrenome? \n")
    dados.append([nome, sobrenome])
    opt = input("\nO que deseja fazer?\n1 Cadastrar\ne- Sair\n")
    print(dados)

with open("3.Aplicações/users.csv", "w", newline="") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)

with open("3.Aplicações/users.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
