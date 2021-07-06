print("Dicionarios")

# O dicionário é definido pelos símbolos { e }
dicionario = {}

# Dicionários não possuem append
# Os valores são adicionados diretamente

dicionario["cat"] = "gato"
dicionario["dog"] = "cachorro"
dicionario["mouse"] = "rato"

print(dicionario)
print(type(dicionario), "\n")

# Dicionários, assim como as listas, são mutáveis:
dicionario["dog"] = "cão"
print(dicionario, "\n")

# Podemos criar o dicionário diretamente também:
dicionario2 = {"Curso": "Online", "Linguagem": "Python", "Módulo": 2}
print(dicionario2, "\n")

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if "cat" in dicionario:
    print("cat existe! \n")

if "bird" in dicionario:
    print("bird existe! \n")

if "gato" in dicionario:
    print("gato existe! \n")


# Função .keys() obtem apenas as chaves
chaves = dicionario.keys()
print(chaves)

# Função .values() obtem apenas os valores
valores = dicionario.values()
print(valores, "\n")

# Função .items() retorna uma lista de tuplas (chave, valor) de um dicionário
itens = dicionario.items()
print(itens)
