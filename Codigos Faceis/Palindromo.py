palavra=input("Escreva a palavra que quer conferir se é um Palindromo ")

palavraContrario=""

i=len(palavra)-1

while i>-1:
    palavraContrario+=str(palavra[i])
    i-=1

if palavra.upper()==palavraContrario.upper():
    print("A palavra é um palindromo")
else:
    print("Nao é um palindromo")
