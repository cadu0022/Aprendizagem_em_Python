#Crie um programa que faça o computador jogar Jokenpô com você

import random
opcoes = ["Pedra", "Papel", "Tesoura"]

random.choice(opcoes)
computador = random.choice(opcoes)
usuario = input("Escolha Pedra, Papel ou Tesoura: ")
print('='*50)
print(f'Você escolheu: {usuario}')
print(f'O computador escolheu: {computador}')

if computador == "Pedra": # pedra que o computador escolheu
    if usuario == "pedra": # pedra que o usuário escolheu
        print("empate!")
    elif usuario == "Papel": # papel que o usuário escolheu
        print("usuario venceu!")                                            #condição 1 - començando com podra
    elif usuario == "Tesoura": # tesoura que o usuário escolheu
        print("Computador venceu!")
    else:
        print("Opção inválida!")
if computador == "Papel": # papel que o computador escolheu
    if usuario == "Papel": # papel que o usuário escolheu
        print("empate!")                                                    #condição 2 - começando com papel
    elif usuario == 'tesoura': # tesoura que o usuário escolheu
        print("computador venceu!")
    elif usuario == "Pedra": # pedra que o usuário escolheu
        print("computador venceu!")
    else:
        print("Opção inválida!")
if computador == "Tesoura": # tesoura que o computador escolheu
    if usuario == "tesoura": # tesoura que o usuário escolheu
        print("empate!")                                                   #condição 3 - começando com tesoura
    elif usuario == "pedra": # pedra que o usuário escolheu
        print("usuario venceu!")
    elif usuario == "papel": # papel que o usuário escolheu
        print("computador venceu!")
    else:
        print("Opção inválida!") # opção inválida caso o usuário digite algo diferente
        