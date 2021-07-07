print("Strings II")

# Operador de soma (+): concatena (une) 2 strings
palavra1 = "Leo"
palavra2 = "nardo"
palavra3 = palavra1 + palavra2
print(palavra3, "\n")

# Operador de multiplicação * copia uma string 'n' vezes
palavra = "uma"
trespalavras = 3 * palavra
print(trespalavras, "\n")

print(".format()")
# .format() serve para preencher os campos em branco de uma string
# Produto substituirá o primeiro {} e preco o segundo {}
produto = "chocolate"
preco = 3.50
print("O produto {} custa {}.\n".format(produto, preco))

# É possível colocar algumas opções especiais de formatação
stringoriginal = "O litro da gasolina custa {:.2f}"
"""
: indica que passaremos opções
.2 indica apenas 2 casas após o ponto decimal
f indica que é um float
O preço sai com apenas 2 casas após a vírgula
"""
preco = 5.505050
stringcompleta = stringoriginal.format(preco)
print(stringcompleta, "\n")

# Pode-se chamar as variávies em diferentes ordens:
print("{2}, {1} and {0}\n".format("a", "b", "c"))

print("{0}{1}{0}\n".format("abra", "cad"))


# Podemos especificar um número de dígitos obrigatório por campo
dia = 1
mes = 8
ano = 2019
data1 = "{}/{}/{}".format(dia, mes, ano)
print(data1, "\n")

# A opção 'd' significa que o parâmetro é um número inteiro
data2 = "{:2d}/{:2d}/{:4d}".format(dia, mes, ano)
print(data2, "\n")

# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:
data3 = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
print(data3, "\n")

# Um modo mais simples de utilizar o format
nome = "Tulio"
profissao = "Professor"
escola = "Faculdade"

print(f"{nome} é {profissao} da {escola}.")
