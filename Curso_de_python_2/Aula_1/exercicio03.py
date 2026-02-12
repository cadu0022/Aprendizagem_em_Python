#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

import random
num1 = random.randint(1,1000000)  
num2 = random.randint(1,1000000)

if num1 >= num2: # verifica se o primeiro número é maior que o segundo
    print(f"O primeiro número ({num1}) é maior que o segundo número ({num2}).")
elif num2 >= num1: # verifica se o segundo número é maior que o primeiro
    print(f"O segundo número ({num2}) é maior que o primeiro número ({num1}).")
else: # verifica se os números são iguais
    print(f"Os números são iguais ({num1}).")