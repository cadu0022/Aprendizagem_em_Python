#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Número: '))
    if num < 0:
        break
    print(f'Tabuada do {num}:')
    for i in range(1, 11):
        print(f'{num} . {i} = {num * i}')
    print()
