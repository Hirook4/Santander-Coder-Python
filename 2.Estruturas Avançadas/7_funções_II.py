print("Funções II")


def somar(n1, n2, n3):
    total = n1 + n2 + n3
    return total


print(somar(3, 3, 3))
print("")


def soma(*args, bonus):
    total = sum(args) + bonus
    return total


print(soma(5, 5, 5, bonus=10))
print("")


def print_info(**kwargs):
    print(kwargs, type(kwargs))


print(print_info(nome="Leonardo", sobrenome="Hirooka"))
