#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import random

numero = random.randint(0,9999)

numero_gerado = f'{numero:4f}'

print(f'numero gerado: {numero}')
print(f'milhar', numero_gerado[0])
print(f'centena', numero_gerado[1])
print(f'dezena', numero_gerado[2])
print(f'unidade', numero_gerado[3])