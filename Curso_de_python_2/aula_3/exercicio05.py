#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números            
#[ 5 ] sair do programa

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

opção  = 0

while opção != 5:
    print('---------MENU----------')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')

    opção = int(input('Escolha uma opção: '))

    if opção == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
    elif opção == 2:
            print(f'O resultado de {valor1} x {valor2} é {valor1 * valor2}')
    elif opção == 3:
            valor_maior = max(valor1, valor2)
            print(f'O maior valor entre {valor1} e {valor2} é {valor_maior}')
    elif opção == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida!')
