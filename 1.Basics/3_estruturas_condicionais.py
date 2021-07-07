print("If Else")
idade2 = 15
altura = 1.80
if idade2 >= 12 and altura >= 1.60:
    print("Você pode entrar na montanha russa. \n")
else:
    print("Você não pode entrar na montanha russa. \n")


print("Elif")
nota = 10

if nota >= 10:
    print("Nota Maxima! \n")
elif nota >= 8:
    print("Nota Alta! \n")
elif nota <= 7 and nota >= 5:
    print("Nota Média \n")
else:
    print("Xiiii... \n")


print("While")
balas = 10

while balas >= 1:
    print("Comeu uma bala, restaram:", balas, "balas")
    balas = balas - 1
    if balas == 0:
        print("")


print("Exemplo de Senha")
senha = input("Digite a Senha")
while senha != "python":
    print("Acesso Negado \n")
    senha = input("Digite a Senha \n")
else:
    print("Acesso Permitido \n")


print("Contador")
contador = 0
repetições = 10
while contador < repetições:
    print(contador)
    contador = contador + 1


print("\n Break")
while True:
    resposta = input("Digite ok: ")
    if resposta == "ok":
        break
