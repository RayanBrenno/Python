import random

# Lista de monstros
monsters = ["Dinossauro Louco", "Cobra", "Demônio Vermelho", "Farfhir", "Fenix"]

# Seleção aleatória do inimigo e pontos de vida
enemy = random.choice(monsters)
mob_life = random.randint(800, 1000)

# Seleção da arma
arma = int(input("Escolha sua arma:\n"
                 "1-Espada\n"
                 "2-Adaga\n"
                 "3-Cajado\n"
                 " "))

if arma == 1:
    per_life = random.randint(850, 1050)
    print(f"Seu inimigo é um {enemy}\n"
          f"Ele tem {mob_life} pontos de vida\n"
          f"E você tem {per_life} pontos de vida\n")

    interation = input("Pronto para a luta?\nSim ou Não?\n").strip().upper()
    if interation == "NÃO" or interation == "NAO":
        print("Fraco!")
        exit()

    while mob_life > 0 and per_life > 0:
        rate_chance_mob = random.randint(0, 20)
        rate_chance_per = random.randint(0, 20)

        # Escolha do ataque
        attack_choice = input("Qual ataque usar?\n"
                              "1-Corta tudo\n"
                              "2-Corta mundo\n"
                              "3-Corta cabeça\n"
                              " ")
        if attack_choice == "1":
            if rate_chance_per < 18:
                damage = random.randint(150, 170)
                mob_life -= damage
                print(f"Você acertou um Corta tudo!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "2":
            if rate_chance_per < 13:
                damage = random.randint(171, 190)
                mob_life -= damage
                print(f"Você acertou um Corta mundo!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "3":
            if rate_chance_per < 8:
                damage = random.randint(210, 240)
                mob_life -= damage
                print(f"Você acertou um Corta cabeça!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")

        if rate_chance_mob > 8:
            attack_mob = random.randint(0, 5)
            if attack_mob == 5:
                damage = random.randint(171, 200)
                per_life -= damage
                print(f"O monstro acertou um ataque crítico!\nSua vida: {per_life}")
            elif attack_mob in [3, 4]:
                damage = random.randint(141, 170)
                per_life -= damage
                print(f"O monstro acertou um bom ataque!\nSua vida: {per_life}")
            else:
                damage = random.randint(110, 140)
                per_life -= damage
                print(f"O monstro acertou um ataque normal!\nSua vida: {per_life}")
        else:
            print(f"O monstro errou o ataque!\nSua vida: {per_life}")

        if mob_life <= 0 and per_life <= 0:
            print("Vocês dois morreram!")
        elif mob_life <= 0:
            print("Parabéns! Você derrotou o monstro!")
        elif per_life <= 0:
            print("Você morreu! PERDEDOR!")
        else:
            input("Pressione 'Enter' para continuar...")

elif arma == 2:
    per_life = random.randint(750, 900)
    print(f"Seu inimigo é um {enemy}\n"
          f"Ele tem {mob_life} pontos de vida\n"
          f"E você tem {per_life} pontos de vida\n")

    interation = input("Pronto para a luta?\nSim ou Não?\n").strip().upper()
    if interation == "NÃO" or interation == "NAO":
        print("Fraco!")
        exit()

    while mob_life > 0 and per_life > 0:
        rate_chance_mob = random.randint(0, 20)
        rate_chance_per = random.randint(0, 20)

        # Escolha do ataque
        attack_choice = input("Qual ataque usar?\n"
                              "1-Sombra negra\n"
                              "2-Voadora dos ceus\n"
                              "3-Assassinato da meia noite\n"
                              " ")
        if attack_choice == "1":
            if rate_chance_per < 18:
                damage = random.randint(160, 180)
                mob_life -= damage
                print(f"Você acertou um Sombra negra!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "2":
            if rate_chance_per < 13:
                damage = random.randint(181, 200)
                mob_life -= damage
                print(f"Você acertou um Voadora dos ceus!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "3":
            if rate_chance_per < 8:
                damage = random.randint(220, 250)
                mob_life -= damage
                print(f"Você acertou um Assassinato da meia noite!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")

        if rate_chance_mob > 8:
            attack_mob = random.randint(0, 5)
            if attack_mob == 5:
                damage = random.randint(171, 200)
                per_life -= damage
                print(f"O monstro acertou um ataque crítico!\nSua vida: {per_life}")
            elif attack_mob in [3, 4]:
                damage = random.randint(141, 170)
                per_life -= damage
                print(f"O monstro acertou um bom ataque!\nSua vida: {per_life}")
            else:
                damage = random.randint(110, 140)
                per_life -= damage
                print(f"O monstro acertou um ataque normal!\nSua vida: {per_life}")
        else:
            print(f"O monstro errou o ataque!\nSua vida: {per_life}")

        if mob_life <= 0 and per_life <= 0:
            print("Vocês dois morreram!")
        elif mob_life <= 0:
            print("Parabéns! Você derrotou o monstro!")
        elif per_life <= 0:
            print("Você morreu! PERDEDOR!")
        else:
            input("Pressione 'Enter' para continuar...")

elif arma == 3:
    per_life = random.randint(670, 860)
    print(f"Seu inimigo é um {enemy}\n"
          f"Ele tem {mob_life} pontos de vida\n"
          f"E você tem {per_life} pontos de vida\n")

    interation = input("Pronto para a luta?\nSim ou Não?\n").strip().upper()
    if interation == "NÃO" or interation == "NAO":
        print("Fraco!")
        exit()

    while mob_life > 0 and per_life > 0:
        rate_chance_mob = random.randint(0, 20)
        rate_chance_per = random.randint(0, 20)

        # Escolha do ataque
        attack_choice = input("Qual ataque usar?\n"
                              "1-Bola de fogo\n"
                              "2-Cubo de gelo\n"
                              "3-Kamehameha\n"
                              " ")
        if attack_choice == "1":
            if rate_chance_per < 18:
                damage = random.randint(180, 200)
                mob_life -= damage
                print(f"Você acertou uma Bola de fogo!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "2":
            if rate_chance_per < 13:
                damage = random.randint(201, 220)
                mob_life -= damage
                print(f"Você acertou um Cubo de gelo!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")
        elif attack_choice == "3":
            if rate_chance_per < 8:
                damage = random.randint(240, 300)
                mob_life -= damage
                print(f"Você acertou um Kamehameha!\nVida do monstro: {mob_life}")
            else:
                print(f"Você errou o ataque!\nVida do monstro: {mob_life}")

        if rate_chance_mob > 8:
            attack_mob = random.randint(0, 5)
            if attack_mob == 5:
                damage = random.randint(201, 220)
                per_life -= damage
                print(f"O monstro acertou um ataque crítico!\nSua vida: {per_life}")
            elif attack_mob in [3, 4]:
                damage = random.randint(141, 170)
                per_life -= damage
                print(f"O monstro acertou um bom ataque!\nSua vida: {per_life}")
            else:
                damage = random.randint(110, 140)
                per_life -= damage
                print(f"O monstro acertou um ataque normal!\nSua vida: {per_life}")
        else:
            print(f"O monstro errou o ataque!\nSua vida: {per_life}")

        if mob_life <= 0 and per_life <= 0:
            print("Vocês dois morreram!")
        elif mob_life <= 0:
            print("Parabéns! Você derrotou o monstro!")
        elif per_life <= 0:
            print("Você morreu! PERDEDOR!")
        else:
            input("Pressione 'Enter' para continuar...")

print("Obrigado por jogar no 'mini joguinho de tabuleiro' ❤️❤️❤️!!!!!!!️ ")
