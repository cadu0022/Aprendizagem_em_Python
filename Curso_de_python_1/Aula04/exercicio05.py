#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('digite um ano qualquer: '))

if ano % 4 == 0:
    print(f'{ano} é ano bissexto')
else:
    print(f'{ano} não é ano bissexto')