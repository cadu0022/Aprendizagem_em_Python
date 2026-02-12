#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_do_fucionario = float(input('salario do fucionario: R$'))

valor_do_aumento = salario_do_fucionario * 0.15
valor_com_aumento_incluso = salario_do_fucionario + valor_do_aumento

print('-' * 50)
print(f'valor do aumento de 15%: R${valor_do_aumento:.2f}')
print(f'salairo com aumento: R${valor_com_aumento_incluso:.2f}')