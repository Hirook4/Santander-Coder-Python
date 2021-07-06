print("Listas")

# Lista vazia
lista_vazia = []

# Listas podem ter diferentes tipos de valores
listamista = [10, "Leonardo", 0.5, True]

# Lista com valores
letras = ["a", "b", "c", "d", "e"]

# Acessamos cada elemento da lista através de um índice entre colchetes
# Os índices começam em 0
print(letras[0])
print(letras[1])
print(letras[2])
print(letras[3])
print(letras[4])

print("\nAlterando valor de um elemento na lista")
# Listas são mutáveis: podemos alterar o valor de seus itens
letras[2] = "Banana"
print(letras)

# Um jeito inteligente de trabalhar com listas é utilizando loops
indice = 0
while indice < len(letras):
    print(letras[indice])
    indice = indice + 1

print("\nAppend")
# Adiciona um elemento na lista

animais = ["Cavalo", "Pato", "Macaco"]
animais.append("Cobra")
print(animais)

print("\nRemove")

print(animais)
animais.remove("Cobra")
print(animais)

print("\nCount")
# Conta quantas vezes um elemento aparece na lista

jogadores = ["Ronaldo", "Rivaldo", "Ronaldo", "Adriano"]
ronaldos = jogadores.count("Ronaldo")
print(jogadores)
print("Quantidade de Ronaldos:", ronaldos, "\n")

print("Tuplas")

# Tupla é uma coleção de objetos que lembra as listas, porem elas são imutáveis

# As tuplas podem ser declaradas com ou sem parênteses
numeros = (1, 2, 3, 5, 7, 11)

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)
