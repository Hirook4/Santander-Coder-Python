print("DictReader e DictWriter")
# Podemos também trabalhar com dicionários, onde a primeira linha é lida como a chave e as demais são os respectivos valores

import csv

with open("3.Aplicações/names.csv", "w", newline="") as csvfile:
    chaves = ["first_name", "last_name"]  # Definimos o Cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves)  # Especificamos o Cabeçalho

    writer.writeheader()  # Escrevemos o Cabeçalho
    # Escrevemos linhas com as chaves e valores
    writer.writerow({"first_name": "Leonardo", "last_name": "Hirooka"})
    writer.writerow({"first_name": "Arthur", "last_name": "Diniz"})
    writer.writerow({"first_name": "Tulio", "last_name": "Calixto"})

with open("3.Aplicações/names.csv", "r") as nomes:
    # A primeira linha é lida como um cabeçalho
    leitor = csv.DictReader(nomes, delimiter=",")
    for linha in leitor:
        # Podemos chamar um valor específico de cada linha pela chave no cabeçallho
        print(linha["first_name"])
