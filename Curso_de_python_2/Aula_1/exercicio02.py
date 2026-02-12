#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('digite um numero: ')) # lê um número inteiro do usuário
print(f'Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL') # apresenta as opções de conversão
opcao = int(input('Sua opção: ')) # lê a opção escolhida pelo usuário

#verifica a opção escolhida e realiza a conversão correspondente
if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)}') # converte o número para binário
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é igual a {oct(num)}') # converte o número para octal
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)}') # converte o número para hexadecimal
else:
    print('Opção inválida!') # mensagem de erro para opção inválida caso o usuário digite uma opção diferente de 1, 2 ou 3
#o programa lê um número inteiro e uma opção de conversão, depois converte o número para a base escolhida pelo usuário

