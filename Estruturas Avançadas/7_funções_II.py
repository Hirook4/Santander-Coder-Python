print("Funções II")


def soma(n1, n2, n3):
    total = n1 + n2 + n3
    return total


def soma(*args, bonus):
    total = sum(args) + bonus
    return total


print(soma(3, 3, 3, bonus=10))
print("")


def print_info(**kwargs):
    print(kwargs, type(kwargs))


print(print_info(nome="Leonardo", sobrenome="Hirooka"))
