print("Strings I")

frase = "uma FRASE"

# Podemos acessar individualmente cada caractere em uma frase
# A ideia é a mesma de acessar uma lista
# Porém, strings são imutáveis: não podemos alterar caracteres individuais
print(frase[0])
print(frase[1])
print(frase[2])

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres \n")


print("String para Lista")
# Podemos converter strings para listas:
listafrase = list(frase)
print(listafrase)

print("Função Join")
# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = "---".join(listafrase)
print(stringfinal)

# Algumas funções que retornam a string "tratada"
# NENHUMA delas ALTERA a string original, elas sempre apenas retornam uma string nova
s1 = frase.capitalize()  # Primeira letra maiúscula e o restante minúscula
s2 = frase.title()  # Início de palavra maiúscula e o restante minúscula
s3 = frase.upper()  # String inteira em maiúscula
s4 = frase.lower()  # String inteira em minúscula
s5 = frase.replace("F", "C")  # Substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print("String original:", frase, "\n")

# Outra possibilidade é quebrar a string em uma lista de substrings
# Sempre que o caractere especificado é encontrado, a string é quebrada
quebra1 = frase.split(" ")  # Quebra a frase no caractere espaço em branco
quebra2 = s3.split("A")  # Quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

# Podemos inserir quebras de linha com '\n'
frase = "uma\nFRASE"
print(frase)
# Podemos inserir tabulação com '\t'
frase = "uma\n\tFRASE"
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = "uma\\FRASE"
print(frase)
