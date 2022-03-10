import random

while True:

    jogador = 4
    computador = random.randint(1, 3)
    resultjogador = ""
    resultcomp = ""

    print("\n1 para Pedra, 2 para papel e 3 para tesoura")

    try:
        while jogador > 3:
            jogador = int(input("\nQual a sua Opção?  "))



    except ValueError:
        print("\nDigite apenas números de 1 a 3")
        break

    if jogador == 1:
        resultjogador = "Pedra"
    elif jogador == 2:
        resultjogador = "Papel"
    else:
        resultjogador = "Tesoura"

    if computador == 1:
        resultcomp = "Pedra"
    elif jogador == 2:
        resultcomp = "Papel"
    else:
        resultcomp = "Tesoura"

    print("\nVocê: "+resultjogador+"\nOponente: "+resultcomp)
    if resultjogador == resultcomp:
        print("\nEmpate!")
    elif resultjogador == "Pedra":
        if resultcomp == "Tesoura":
            print("\nVocê Ganhou!")
        else:
            print("\nVocê Perdeu...")
    elif resultjogador == "Papel":
        if resultcomp == "Pedra":
            print("\nVocê Ganhou!")
        else:
            print("\nVocê Perdeu...")
    else:
        if resultcomp == "Papel":
            print("\nVocê Ganhou!")
        else:
            print("\nVocê Perdeu...")

    play_again = input("\nJogar novamente? (s/n): ")
    if play_again.lower() != "s":
        break