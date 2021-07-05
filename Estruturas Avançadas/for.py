print("For")
num = [1, 2, 3, 4, 5, 6]
for elemento in num:
    print(elemento)
print("")

local = {
    'cidade': 'Ribeirão Preto',
    'estado': 'São Paulo',
    'pais': 'Brazil'
}
for chave in local:
        print(f'{chave}: {local[chave]}')

print("\nRange com 1 parâmetro, ele será interpretado como valor final (exclusivo)")
for numero in range(15):
    print(numero)
print("")


print(
    "Range com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o segundo será o final (exclusivo)."
)
for numero in range(5, 20):
    print(numero)
print("")

print("Range com 3 parâmetros, o terceiro será interpretado como incremento")
for numero in range(1, 20, 2):
    print(numero)
print("")


print("também  pode ser decremento")
for numero in range(10, 0, -1):
    print(numero)
