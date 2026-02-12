#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar.

dinheiro_em_reais = float(input('digite a quantidade: '))

dollar = 5.52
quantidade_a_comprar = dollar * dinheiro_em_reais 

print(f'valor do dollar= {dollar} \nquantidade comprada= {quantidade_a_comprar:.2f}')