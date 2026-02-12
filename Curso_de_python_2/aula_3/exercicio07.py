#lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('a1: '))
razao = int(input('R: '))

n = 1
while n <= 10:
    termo = primeiro_termo + (n - 1) * razao
    n += 1
    print(f'{n} : {termo}') 
   