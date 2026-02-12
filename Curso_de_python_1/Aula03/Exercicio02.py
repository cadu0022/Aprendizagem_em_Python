#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

import math
num1 = float(input('cateto oposto:'))
num2 = float(input('cateto adjacente:'))
num3 = str(input('hipotenusa:'))

num3 = math.trunc(math.sqrt(num1 ** 2 + num2 ** 2))

print(f'{num3}')