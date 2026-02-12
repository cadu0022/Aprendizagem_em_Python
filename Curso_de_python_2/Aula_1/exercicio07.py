#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– ESCALENO: todos os lados diferentes
#– ISÓSCELES: dois lados iguais, um diferente
#– EQUILÁTERO: todos os lados iguais

print('='*50)
print('Analisador de Triângulos')

import random 
a = int(input('Digite o valor do primeiro segmento: '))
b = int(input('Digite o valor do segundo segmento: '))
c = int(input('Digite o valor do terceiro segmento: '))
# = random.randint(0,50)
# = random.randint(0,50)
# = random.randint(0,50)
# pode usar o random para gerar valores aleatórios ou input para o usuário digitar os valores
print(f'Os segmentos medem: {a}, {b}, {c}') #mostra os valores dos segmentos para o usuário
if a + b > c and b + a > c and c + a > b: #condição para formar um triângulo
    if a != b != c != a: # condição para triângulo escaleno
        tipo = 'ESCALENO' # tipo do triângulo
    elif a == b == c:# condição para triângulo equilátero
        tipo = 'EQUILÁTERO' # tipo do triângulo
    elif a == b != c or a == c != b or b == c != a: # condição desta forma garante que um dos lados seja diferente. testanto todas as combinações possíveis usando 'ou'
        tipo = 'ISÓSCELES'
    print(f'Os segmentos acima PODEM FORMAR um triângulo do tipo {tipo}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')


#OBS: END='' NO PRINT PARA NÃO QUEBRAR A LINHA. OU SEJA , CONTINUAR NA MESMA LINHA.
#PRINT('TESTE', end=' ') -> DEPENDODO DA LARGUDA DO ENTRE ASPAS, VAI DAR UM ESPAÇO MAIOR OU MENOR
#PRINT('TESTE2')
#SAIDA: TESTE TESTE 2