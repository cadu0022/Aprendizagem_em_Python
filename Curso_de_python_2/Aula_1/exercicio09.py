#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

produto = float(input("Digite o preço do produto: R$ "))
print("Escolha a forma de pagamento:")
print("1 - À vista no cartão (5% de desconto)")
print("2 - Em até 2x no cartão (preço formal)")
print("3 - 3x ou mais no cartão (20% de juros)")

pagamento = int(input("Digite o número da forma de pagamento: "))

a_vista = produto - (produto * 0.05)
duas_vezes = produto / 2
tres_ou_mais = (produto + (produto * 0.20)) / pagamento


if pagamento == 1:
    print(f"Valor a ser pago: R$ {a_vista:.2f}")
elif pagamento == 2:
    print(f"Valor a ser pago: R$ {duas_vezes:.2f} em 2x")
elif pagamento >= 3:
    print(f"Valor a ser pago: R$ {tres_ou_mais:.2f} em {pagamento}x")
else:
    print("Forma de pagamento inválida.")