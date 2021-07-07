print("Funções")

print("Função sem parâmetro")


def hello():
    print("Hello World \n")


hello()


print("Função com parâmetros")


def ola(nome, sobrenome):
    print("Olá", nome, sobrenome)


ola("Leonardo", "Hirooka \n")

print("Função com parâmetros e format")


def dadosPessoais(nome, idade, cidade):
    print(f"Seu nome é {nome}, você tem {idade} anos e mora em {cidade} \n")


dadosPessoais("Thamiris", 19, "Serrana")

print("Funções com respostas")


def somar(n1, n2):
    return n1 + n2


print(somar(10, 5))


def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma


numeros = [1, 2, 3, 4, 50]
total = somatorio(numeros)
print("A soma dos elementos da lista vale: ", total)

if somatorio(numeros) > 50:
    print("Deu mais de 50 \n")
else:
    print("Deu menos de 50 \n")


print("Funções Recursivas")


def funcaoRecursiva(numero):
    if numero != 1:
        funcaoRecursiva(numero - 1)
    print(numero)


print("Testando a função recursiva:")
funcaoRecursiva(10)
