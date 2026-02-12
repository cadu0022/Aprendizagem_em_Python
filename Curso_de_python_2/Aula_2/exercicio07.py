#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
limite = int(input('Digite até qual número você quer ver os primos: '))

for num in range(1, limite + 1):  
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')