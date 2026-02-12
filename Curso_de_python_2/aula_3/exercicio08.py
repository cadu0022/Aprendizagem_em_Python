n = 0  # contador 
while True: #estrutura de repetição -> enquanto for verdadeiro
    n = int(input('digite um numero: '))
    if n >= 10: # condições de parada 
        break # parar repetição caso o número seja maior ou igual a 10
    na = n + 1 # soma so acontece enquanto menor que 10, ai ele faz a soma, e para a repetição
    
    print(f' numero digitado {n}, rersultado da soma{na}')

