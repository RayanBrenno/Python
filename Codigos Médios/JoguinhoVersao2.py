# Joguinho melhorado e mais bonito
import random

def combat(nome_monstro, vida_monstro, vida_jogador, ataques):
    print(f"Seu inimigo é um {nome_monstro}")
    print(f"Ele tem {vida_monstro} pontos de vida")
    print(f"E você tem {vida_jogador} pontos de vida")

    ready = input("Pronto para a luta? (Sim ou Não): ").strip().upper()
    if ready != "SIM":
        print("Fraco!")
        return

    while vida_monstro > 0 and vida_jogador > 0:
        rate_chance_mob = random.randint(0, 20)

        print("Select your attack:")
        print("1:", ataques[0])
        print("2:", ataques[1])
        print("3:", ataques[2])

        ataque_escolhido = input("Digite sua escolha (1, 2 ou 3): ").strip()

        if ataque_escolhido in ['1', '2', '3']:
            dano = random.randint(ataques[int(ataque_escolhido) - 1][0], ataques[int(ataque_escolhido) - 1][1])
            vida_monstro -= dano
            print(f"You hit a {ataques[int(ataque_escolhido) - 1][2]}! Monster's life: {vida_monstro}")
        else:
            print("Invalid choice!")

        if vida_monstro <= 0:
            print("Congrats! You defeated the monster!\n"
                  "Thanks for playing")
            break

        if rate_chance_mob > 8:
            ataque_monstro = random.randint(0, 5)
            if ataque_monstro == 5:
                dano_monstro = random.randint(171, 200)
            elif ataque_monstro == 3 or ataque_monstro == 4:
                dano_monstro = random.randint(141, 170)
            else:
                dano_monstro = random.randint(110, 140)
            vida_jogador -= dano_monstro
            print(f"O monstro acertou você! Sua vida: {vida_jogador}")
        else:
            print("O monstro errou o ataque\n")

        if vida_jogador <= 0:
            print("Você morreu! PERDEDOR!")
            break

# Monster options
monsters = ["Dinossauro Louco", "Cobra", "Demônio Vermelho", "Farfhir", "Fenix"]

# arma  ataques
ataques_espada = [(150, 170, "Corta Tudo"), (171, 190, "Corta mundo"), (210, 240, "Corta cabeça")]
ataques_adaga = [(160, 180, "Sombra negra"), (181, 200, "Voadora dos ceus"), (220, 250, "Assassinato da meia noite")]
ataques_cajado = [(180, 200, "Bola de fogo"), (201, 220, "Cubo de gelo"), (240, 300, "Kamehameha")]

# arma  selection
arma  = int(input("Escolha sua arma:\n"
                 "1-Espada\n"
                 "2-Adaga\n"
                 "3-Cajado\n"
                 " "))

# Mob and player life points
vida_monstro = random.randint(800, 1000)

if arma  == 1:
    vida_jogador = random.randint(850, 1050)
    combat(random.choice(monsters), vida_monstro, vida_jogador, ataques_espada)
elif arma  == 2:
    vida_jogador = random.randint(750, 900)
    combat(random.choice(monsters), vida_monstro, vida_jogador, ataques_adaga)
elif arma  == 3:
    vida_jogador = random.randint(670, 860)
    combat(random.choice(monsters), vida_monstro, vida_jogador, ataques_cajado)
