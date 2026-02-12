#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre 
#quantas pessoas ainda não atingiram a maioridade e quantas já são mais
import random 
import datetime

ano_atual = datetime.date.today().year

total_maior = 0
total_menor = 0

for pessoa in range(1, 8):
    ano_nascimento = random.randint(2000, 2026)  # Simulando o ano de nascimento
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        total_maior += 1
        print(f'Pessoa {pessoa}: {idade} anos - Maior de idade')
    else:
        total_menor += 1
        print(f'Pessoa {pessoa}: {idade} anos - Menor de idade')