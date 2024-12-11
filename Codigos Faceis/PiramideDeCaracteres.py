import random


def piramide(qtdLinha):
    for x in range(1, qtdLinha+1):
        if qtdLinha-x != 0:
            print(" "*((qtdLinha)-x-1), "* "*x)
        else:
            print("* "*x)


def piramideUmlado(qtdLinha):
    for x in range(1, qtdLinha+1):
        print("*"*x)
    for x in range(1, qtdLinha+1):
        if qtdLinha-x != 0:
            print(" "*((qtdLinha)-x-1), "*"*x)
        else:
            print("*"*x)


def piramideEmV(qtdLinha):
    for x in range(1, qtdLinha+1):
        aux = "*"*x
        if qtdLinha-x != 0:
            print(aux + (" "*((qtdLinha)-x)*2) + "*"*x)
        else:
            print(aux+("*"*x))


qtdLinha = random.randint(5, 10)
piramide(qtdLinha)
piramideUmlado(qtdLinha)
piramideEmV(qtdLinha)
