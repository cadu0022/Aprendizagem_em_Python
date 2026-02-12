#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import datetime # From datetime importa a classe datetime. ou seja importando apenas a classe datetime da biblioteca datetime

data_nascimento = input("Data: ") # digita a data no formato ddmmyyyy -> string para o usuario relacionada a data
data = datetime.strptime(data_nascimento,"%d%m%Y") #converte a string para o formato de data -> ou seja a string que era um texto passa a ser um objeto data
print(data.strftime("%d/%m/%Y")) # strftime é a formatação de texto (str) que passa passsa a ser um objeto data

ano_nascimento = data.year # ele mostra apenas o ano da data fornecida
ano_atual = datetime.now().year #datatime.now pega a data atual e .year pega o ano atual
atleta_idade = ano_atual - ano_nascimento # idade do atleta, subtraindo o ano atual pelo ano de nascimento
print(f'idade do atleta: {atleta_idade} anos') # mostra ao usuario a idade do atleta que foi subtraida

if atleta_idade <= 9: # Uma condição se a idade do atleta é menor ou igual a 9 anos
    print('atleta mirim') # se a condição for verdadeira mostra ao usuario a categoria do atleta
elif atleta_idade <= 14: # Uma condição se a idade do atleta é menor ou igual a 14 anos
    print('atleta infantil') # se a condição for verdadeira mostra ao usuario a categoria do atleta
elif atleta_idade <= 19: # Uma condição se a idade do atleta é menor ou igual a 19 anos
    print('atleta junior') # se a condição for verdadeira mostra ao usuario a categoria do atleta
elif atleta_idade <= 25: # Uma condição se a idade do atleta é menor ou igual a 25 anos
    print('atleta sênior') # se a condição for verdadeira mostra ao usuario a categoria do atleta
elif atleta_idade > 25: # Uma condição se a idade do atleta é maior que 25 anos
    print('atleta profissional') # se a condição for verdadeira mostra ao usuario a categoria do atleta
else:
    print('idade inválida') # se nenhuma das condições anteriores forem verdadeiras, mostra ao usuario que a idade é inválida
