#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_do_produto = float(input('Valor do produto: R$ '))

valor_do_desconto = valor_do_produto * 0.05
valor_com_desconto = valor_do_produto - valor_do_desconto

print('-' * 50)
print(f'Valor do desconto: R$ {valor_do_desconto:.2f}')
print(f'Valor com desconto: R$ {valor_com_desconto:.2f}')