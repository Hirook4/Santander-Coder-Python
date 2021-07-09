print("Arquivos CSV")

# CSV (Comma Separated Values, ou Valores Separados por Vírgula) é um arquivo de texto que representa dados em tabela
# Cada linha do arquivo é uma linha da tabela e as colunas são separadas por vírgulas
# Poderíamos manipular esses arquivos diretamente usando as funções de arquivo vistas anteriormente.

1, 2, 3, 4

5, 6, 7, 8

9, 10, 11, 12

# É normal que outros separadores sejam usados ao invés de vírgula, como ; para permitir que a vírgula seja usada em um campo
# Existe um módulo em Python para manipular arquivos CSV que nos ajuda a tratar essas diferenças
# Todo programa que for utilizar o módulo CSV deverá importá-lo em seu início através do comando "import csv"

import csv
# Criando um CSV
with open("3.Aplicações/tabelaExemplo.csv", "w") as arquivo:
    # Criando um Escritor
    escritor = csv.writer(arquivo, delimiter=";", lineterminator="\n")
    # writerows escreve cada "sublista" da lista como uma linha
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escritor.writerows(lista)


# Lendo um CSV
with open("3.Aplicações/tabelaExemplo.csv", "r") as arquivo:
    # Criando um Leitor
    leitor = csv.reader(arquivo, delimiter=";", lineterminator="\n")
    print("O conteúdo do arquivo é:")
    print(leitor)
    for linha in leitor:
        print(linha)
