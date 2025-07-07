'''
jOGO DAS FRUTAS 
Alcides Diniz
2025.07.02
'''
#Objetivo: Adivinhar a fruta
import random

# Lista de frutas e suas dicas
frutas = {
    "banana": ["Sou amarela", "Sou curvada", "Macacos adoram"],
    "maçã": ["Sou vermelha ou verde", "Muito presente em contos de fadas", "Uma por dia mantém o médico longe"],
    "laranja": ["Sou cítrica", "Tenho muita vitamina C", "Minha cor é meu nome"],
    "uva": ["Sou pequena", "Cresço em cachos", "Vinho vem de mim"],
    "abacaxi": ["Sou espinhoso por fora", "Doce por dentro", "Tropical e refrescante"],
    "melancia": ["Sou grande", "Tenho muita água", "Verde por fora e vermelha por dentro"]
}

def jogar():
    print("\n Bem-vindo ao jogo: Adivinhe a Fruta!")
    fruta, dicas = random.choice(list(frutas.items()))
    print("\n Bem-vindo ao jogo: Adivinhe a Fruta!")
    print("Você terá 3 dicas para descobrir qual é a fruta. Vamos lá!\n")

    for i, dica in enumerate(dicas):
        print(f"Dica {i+1}: {dica}")
        palpite = input("Qual fruta você acha que é? ").strip().lower()

        if palpite == fruta:
            print(f"\n Parabéns! Você acertou! A fruta é {fruta}.")
            break
        else:
            print(" Errado!\n")
    else:
        print(f"Que pena! As dicas acabaram Bobão. A fruta era: {fruta}.")

# Loop principal para jogar novamente
while True:
    jogar()
    jogar_novamente = input("\n Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        print(" Obrigado por jogar! Até a próxima!")
        break
