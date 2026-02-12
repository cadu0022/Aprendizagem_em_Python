import random
par = 0 
impar = 0
n = 1
while n != 0:
    n = random.randint(0, 100)
    if n % 2 == 0:
        par += 1
        print(f'{n} é par')
    else:
        impar += 1
        print(f'{n} é impar')
print('fim')  
print(f'Quantidade de números pares: {par}')
print(f'Quantidade de números ímpares: {impar}')