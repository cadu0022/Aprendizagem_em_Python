#mostre ao usuario a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('digite um numero: ')) # input -> variável que o usuario coloca.
for i in range(0, 11): # intervalo, que tbm pode ser modificado para que o usuario escolha o intervalo
    print(f'{n} x {i} = {n * i}')
# print = format -> n = input digitado x i -> range (intervalo) = n * i = resultado
#