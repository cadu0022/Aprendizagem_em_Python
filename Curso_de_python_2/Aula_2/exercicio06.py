#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#an: termo que queremos calcular
#a1: primeiro termo da P.A.
#n: posição do termo que queremos descobrir
#r: razão

primeiro_termo = int(input('a1: '))
razao = int(input('R: '))

for n in range(1, 11): 
    termo = primeiro_termo + (n - 1) * razao
    print(f'{n} : {termo}')