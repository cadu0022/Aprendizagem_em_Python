#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

n = 3
for i in range(1, 500):
    if i % n == 0: # se i for (% -> resto) 0, logo é multiplo de 3
        print(f"{i} é múltiplo de {n}") # mostra ao usuario o numero do intervalo e 3 caso for multiplo de 3 
        