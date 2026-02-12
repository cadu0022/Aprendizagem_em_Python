#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: ')) # digite um número -> variavel num

dobro = num * 2 #dobro recebe num (*) 2
triplo = num * 3 #triplo recebe num (*) 3
raiz = num ** (1/2) #raiz recebe num elevado a (1/2) -> raiz quadrada

print(f'Dobro = {dobro}\nTriplo = {triplo}\nRaiz = {raiz}')# mostra na tela o dobro, triplo e raiz quadrada do número.