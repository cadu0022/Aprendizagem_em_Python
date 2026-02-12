#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random #import de biblioteca random (gera numeros entre outros)

print('sorteiro para apagar o quadro')
print('-'*35)

alunos = ['carlos', 'samyra', 'felipe' , 'leo']
#alunos que serão sorteados

escolha = random.choice(alunos)
#random choice serve para seleciona elementos dentro de uma lista

print(f'o aluno escolhido foi:{escolha}')
#aparece na tela os nome escolhido
 