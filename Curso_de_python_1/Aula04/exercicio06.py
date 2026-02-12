#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from random import randint
num1 = randint(0,9999)
num2 = randint(0,9999)
num3 = randint(0,9999)
print(f'Numeros gerados: {num1}, {num2} , {num3}')
#maior
if num1 > num2: 
    if num1 > num3: 
        maior = num1 
else:
    if num2 > num3:
        maior = num2 
    else:
        maior = num3 

#menor
if num1 < num2:
    if num1 < num3:
        menor = num1
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print(f'maior numero é: {maior}')
print(f'menor numero é: {menor}')