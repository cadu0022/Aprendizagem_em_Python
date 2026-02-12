#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o sexo da pessoa: "))

while sexo not in 'MmFf':
    sexo = str(input("dados invalidos. Digite o sexo da pessoa: "))
print(f'sexo {sexo} registrado com sucesso.')