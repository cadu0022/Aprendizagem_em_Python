#O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.

#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

# Lista de alunos
alunos = ['carlos', 'leo', 'samyra', 'flavia']
#import para embaralhar as variaves
random.shuffle(alunos)
#mostra na tela os alunos em ordem.
print('Ordem de alunos para apresentação')
print(f'primeiro: {alunos[0]}')
print(f'segundo: {alunos[1]}')
print(f'terceiro: {alunos[2]}')
print(f'quarto: {alunos[3]}')




