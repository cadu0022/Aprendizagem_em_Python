#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

import random

pesos = []

for i in range(1, 6):
    peso = random.uniform(50.0, 100.0)  # Simulando a leitura do peso com um valor aleatório
    pesos.append(peso)
    print(f'Peso da pessoa {i}: {peso:.2f} kg')


