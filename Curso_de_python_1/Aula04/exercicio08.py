#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#a condição de existência é que a medida de cada lado seja menor que a soma das medidas dos outros dois lados
#aninhamento de estruturas condicionais


import random

a = random.randint(0,50)
b = random.randint(0,50)
c = random.randint(0,50)

print(f'{a}, {b}, {c}')

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('pode forma um triangulo')
        else:
            print('Não pode forma triangulo')
    else:
        print("Não pode formar um triângulo")
else:
    print("Não pode formar um triângulo")