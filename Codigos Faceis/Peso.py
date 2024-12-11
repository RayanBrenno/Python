weight = float(input("Digite seu peso aqui: "))
tipe = input("Seu peso está em (K)g ou (L)bs? ")

if tipe.upper() == "K":
    print("Seu peso em Lbs é " + str(weight * 2.2))
elif tipe.upper() == "L":
    print("Seu peso em Kg é " + str(weight / 2.2))
else:
    tipe = input("Digite 'K' para KG e 'L' para Lbs: ")
    if tipe.upper() == "K":
        print("Seu peso em Lbs é " + str(weight * 2.2))
    elif tipe.upper() == "L":
        print("Seu peso em Kg é " + str(weight / 2.2))
