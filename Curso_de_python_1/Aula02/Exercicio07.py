#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('digite um numero: ' ))

for i in range (1, 11): # i -> variavel (inteiro), vai de 1 até 11
    print(f'{num} * {i} = {num * i}') # num * numero da tabuada repetidas pela variavel i, que vai de 1 a 10
# Exemplo: 5 * 1 = 5
#          5 * 2 = 10
#          5 * 3 = 15
#          5 * 4 = 20
#          5 * 5 = 25
#          5 * 6 = 30
#          5 * 7 = 35
#          5 * 8 = 40
#          5 * 9 = 45
#          5 * 10 = 50
