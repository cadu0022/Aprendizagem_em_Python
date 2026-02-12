#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

import random

pessoas = {
    'Ana': 'feminino', 
    'Bruno': 'masculino',
    'Carla': 'feminino',
    'Daniel': 'masculino',
    'Eva': 'feminino',
    'Fernando': 'masculino',
    'Gabriela': 'feminino'
}
nome = random.sample(list(pessoas), 4)
for i, nome in enumerate(nome, start=1):
    sexo = pessoas[nome]
    idade = random.randint(10, 60)
    print(f'pessoa {i+1}: {nome}, Idade: {idade}, Sexo: {sexo}')