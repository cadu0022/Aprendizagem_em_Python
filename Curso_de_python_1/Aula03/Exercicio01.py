#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('valor real: '))

inteiro = math.trunc(num)

print(f'valor inteiro: {inteiro}')
