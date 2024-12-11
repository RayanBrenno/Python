# Gerador de Senhas
import random

# Loop para pedir quantidade de algarismos
while True:
    numeroDeAlgorismos = input("Deseja que sua senha tenha quantos algarismos? ")
    if numeroDeAlgorismos.isdigit():
        break
    else:
        print("A quantidade de algarismos deve ser um número!!")

# Loop para pedir o tipo de algarismos
while True:
    tipo = input("Deseja que sua senha tenha:\n"
                 "1-Letras, números e símbolos\n"
                 "2-Letras e números\n"
                 "3-Letras e símbolos\n"
                 "4-Números e símbolos\n"
                 "5-Letras\n"
                 "6-Números\n"
                 "7-Símbolos\n"
                 "")

    if tipo.isdigit() and 1 <= int(tipo) <= 7:
        break
    else:
        print("Escolha um dos tipos!!")

# Loop para pedir o tipo das letras
while True:

    if int(tipo) in [4, 6, 7]:
        break

    tamanho = input("Quer que as letras sejam: \n"
                    "1-Maiúscula e Minúscula\n"
                    "2-Minúscula\n"
                    "3-Maiúscula\n"
                    "")
    if tamanho.isdigit() and 1 <= int(tamanho) <= 3:
        break
    else:
        print("Escolha um dos tipos!!")

opcoesDeAlgorismo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                     "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "&"]

senha = ""
n = 0

#Funções

def tipo_1(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):

    while n < int(numeroDeAlgorismos):
        y = random.randint(0, 1)
        x = random.randint(0, 40)
        if y == 0:
            senha += opcoesDeAlgorismo[x]
            n += 1
        else:
            senha += opcoesDeAlgorismo[x].upper()
            n += 1

    if tamanho == "1":
        return senha

    elif tamanho == "2":
        return senha.lower()

    else:
        return senha.upper()

def tipo_2(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):

    while n < int(numeroDeAlgorismos):
        y = random.randint(0, 1)
        x = random.randint(0, 35)
        if y == 0:
            senha += opcoesDeAlgorismo[x]
            n += 1
        else:
            senha += opcoesDeAlgorismo[x].upper()
            n += 1

    if tamanho == "1":
        return senha

    elif tamanho == "2":
        return senha.lower()

    else:
        return senha.upper()

def tipo_3(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):

    while n < int(numeroDeAlgorismos):
        k = random.randint(0, 1)
        y = random.randint(0, 1)
        if y == 1:
            x = random.randint(0, 25)
        else:
            x = random.randint(35, 40)
        if k == 0:
            senha += opcoesDeAlgorismo[x]
            n += 1
        else:
            senha += opcoesDeAlgorismo[x].upper()
            n += 1

    if tamanho == "1":
        return senha

    elif tamanho == "2":
        return senha.lower()

    else:
        return senha.upper()

def tipo_4(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):
    while n < int(numeroDeAlgorismos):
        x = random.randint(26, 40)
        senha += opcoesDeAlgorismo[x]
        n += 1
    return senha

def tipo_5(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):
    while n < int(numeroDeAlgorismos):
        y = random.randint(0, 1)
        x = random.randint(0, 25)
        if y == 0:
            senha += opcoesDeAlgorismo[x]
            n += 1
        else:
            senha += opcoesDeAlgorismo[x].upper()
            n += 1

    if tamanho == "1":
        return senha
    elif tamanho == "2":
        return senha.lower()
    else:
        return senha.upper()

def tipo_6(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):
    while n < int(numeroDeAlgorismos):
        x = random.randint(26, 35)
        senha += opcoesDeAlgorismo[x]
        n += 1
    return senha

def tipo_7(n, senha, numeroDeAlgorismos, opcoesDeAlgorismo):
    while n < int(numeroDeAlgorismos):
        x = random.randint(36, 40)
        senha += opcoesDeAlgorismo[x]
        n += 1
    return senha

funcoes_tipos = {
    1: tipo_1,
    2: tipo_2,
    3: tipo_3,
    4: tipo_4,
    5: tipo_5,
    6: tipo_6,
    7: tipo_7
}

senha_gerada = funcoes_tipos[int(tipo)](n, senha, numeroDeAlgorismos, opcoesDeAlgorismo)
print(senha_gerada)