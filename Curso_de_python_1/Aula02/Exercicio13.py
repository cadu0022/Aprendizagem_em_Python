#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('-'* 20)
print('Car Rental Service')
print('-'*20) 

km_percorridos = int(input('digite o km: '))
dias_alugados = int(input('digite o dias alugados: '))
print('-'*20)

valor_fixo_por_dia = 60
valor_fixo_por_km = 0.15

aluguel_por_dia = valor_fixo_por_dia * dias_alugados
aluguel_por_km = valor_fixo_por_km * km_percorridos

print(f'aluguel do carro: R${aluguel_por_dia}')
print(f'aluguel a pagar por km: R${aluguel_por_km}')
print(f'aluguel a pagar: R${aluguel_por_dia + aluguel_por_km}')