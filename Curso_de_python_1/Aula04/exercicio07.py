#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep

salario = float(input('salário: '))

reajuste_1 = salario * 0.10
reajuste_2 = salario * 0.15

sleep(2)
if salario > 1250.00 :
    print(f'reajuste de R${salario * 0.15}')
    print(f'salario R$: {reajuste_1 + salario}')
else: 
    if salario <= 1250:
        print(f'reajuste de R$: {salario * 0.15}')
        print(f'salario R$: {reajuste_2 + salario}')
    else:
        print('Não há reajuste disponivel!')