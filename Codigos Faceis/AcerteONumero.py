# ACERTANDO O NUMERO - é um jogo feito usando lógica de programação, que baseia-se em sortear um numero aletorio em um intervalo determinado pelo usuario, logo apos o usuario tem que dar palpites qual o numero sorteado.

import random

n1 = input("Escolha o intervalo que deseja sortear o número\n"
           "Numero menor = ")
n2 = input("Numero maior = ")
numero = random.randint(int(n1), int(n2))
qtDeTent = 1
chutes = input(f"Tente advinhar o número sorteado entre {n1} e {n2} \n"
               "Tentativa 1- ")
n = 0
while True:
    if int(chutes) > int(n2) or int(chutes) < int(n1):
        print(f"Seu palpite deve estar entre {n1} e {n2}")
        chutes = input("De outro palpite\n"
                       "Tentativa " + str(qtDeTent) + "- ")
    elif int(chutes) < numero:
        print("O número sorteado é maior")
        qtDeTent += 1
        chutes = input("Tentativa " + str(qtDeTent) + "- ")
    elif int(chutes) > numero:
        qtDeTent += 1
        print("O número sorteado é menor ")
        chutes = input("Tentativa " + str(qtDeTent) + "- ")
    else:
        print("Você acertou, Parabéns!!!\n"
              "A quantidade de tentativas foi " + str(qtDeTent))
        break

if qtDeTent <= 7:
    print("Parabéns, seu desempenho foi ótimo")
if qtDeTent > 7 and qtDeTent <= 12:
    print("Parabéns, seu desempenho foi bom")
if qtDeTent > 12:
    print("Seu desempenho não foi nada satisfatório, melhore!")
