# Crie um programa que leia o nome completo de uma pessoa e mostra o nome com todas as letra em maiusculo e minusculoquantas letra tem ao todo(sem considerar espaços) quantas letras tem o primeio nome

nome = input("Digite seu nome completo\n"
             "")

qtdPrimeiroNome = 0
qtdLetrasTotal = 0
x = 0
y = 0
print(nome.upper())
print(nome.lower())

while x < len(nome):
    if nome[x] != " ":
        qtdLetrasTotal += 1
        x += 1
    else:
        x += 1

while y < len(nome):
    if nome[y] != " ":
        qtdPrimeiroNome += 1
        y += 1
    else:
        y += 100

print("A quantidade de letras no total é "+str(qtdLetrasTotal))
print("A quantidade de letras do seu primeiro nome é "+str(qtdPrimeiroNome))

# -----------------------------------------------------------------------------

nome = input("Digite seu nome completo: ")

palavras = nome.split()
print(nome.split())
primeiroNome = palavras[0]
ultimoNome = palavras[-1]

if len(palavras) > 2:
    nomeDoMeio = " ".join(palavras[1:-1])
    print("O primeiro nome é", primeiroNome)
    print("O nome do meio é", nomeDoMeio)
    print("O último nome é", ultimoNome)
else:
    print("O primeiro nome é", primeiroNome)
    print("O último nome é", ultimoNome)
