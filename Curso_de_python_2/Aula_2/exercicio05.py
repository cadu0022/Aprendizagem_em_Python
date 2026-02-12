#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
import random
print('-' * 50)
for i in range(6):
    n = random.randint(0,100)
    if n % 2 == 0:
        print(f'{n} é par, e a soma {n + n}')
    else: 
        print(f'{n} é impar')
print('-' * 50)   

