#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('digite um nome: '))

nome_completo = nome.split() 
print('primeiro nome', nome_completo[0])
print('ultimo nome', nome_completo[-1])