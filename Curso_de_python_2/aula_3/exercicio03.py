#melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random 

computador = random.randint(0,10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
        print('acertou')  
    elif jogador != computador:
        print('errou tente novamente')
print(f'voce precisou de {palpites} tentativas para acertar')