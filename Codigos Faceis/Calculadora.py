conta=input("Coloque o calculo que deseja fazer\n"
            " '+' -> Somar\n"
            " '-' -> Subtrair\n"
            " '*' -> Multiplicar\n"
            " '/' -> Dividir\n"
            " ")

n1=float(input("Digite o primeiro numero "))
n2=float(input("Digite o segundo numero "))

if conta=="+":
    print(n1+n2)
elif conta=="-":
    print(n1-n2)
elif conta=="*":
    print(n1*n2)
elif conta=="/":
    print(n1/n2)
    
    