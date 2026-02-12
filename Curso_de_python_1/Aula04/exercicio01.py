#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
numero = randint(0,5)

print('Vou escolher um numero entre 0 e 5, tente adivinhar!')
print('-'* 50)
palpite = int(input('Que numero eu pensei?: '))
print('-'* 50)
print('Processando...')
sleep(2)
if palpite == numero:
    print('Parabens, voce me venceu!')
else:
    print(f'Ganhei! eu pensei no numero {numero} e não no {palpite}')

