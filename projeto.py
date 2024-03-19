import random
from random import randint
def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro =  random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)
    rodada = 1
    while True:
        print("rodada", rodada )
        print("aventureiro: vida" ,vida_aventureiro, "- at", ataque_aventureiro, "- deff", defesa_aventureiro)
        print("monstro: vida" ,vida_monstro, "- att", ataque_monstro)
        vida_monstro = randint(1, ataque_aventureiro)
        vida_aventureiro = randint(1,ataque_monstro) - defesa_aventureiro
        dano_aventureiro = randint (1, ataque_aventureiro)
        dano_monstro = randint (1, ataque_monstro) - defesa_aventureiro


        if dano_monstro < 0:
            dano_monstro = 0

        vida_monstro -= dano_aventureiro
        vida_aventureiro -= dano_monstro
        rodada += 1

        if vida_monstro <= 0:
            print("o monstro morreu")
            break
        print("rodada", rodada )
        print("aventureiro: vida" ,vida_aventureiro, "- at", ataque_aventureiro, "- deff", defesa_aventureiro)
        print("monstro: vida" ,vida_monstro, "- att", ataque_monstro)

main()
