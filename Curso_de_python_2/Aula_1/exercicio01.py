#condições de aninhamento

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o salário do comprador: R$ ")) 
anos_de_pagamento = float(input("Digite em quantos anos o comprador vai pagar a casa: "))

prestacao_mensal = valor_casa / (anos_de_pagamento * 12) # cálculo da prestação mensal - valor da casa dividido pelo número total de meses
limite_prestacao = salario_comprador * 0.3 # 30% do salário do comprador

if prestacao_mensal <= limite_prestacao: # verifica se a prestação mensal está dentro do limite permitido, ou seja dentro dos 30% do salário
    print("Empréstimo aprovado!")
    print(f"O valor da prestação mensal será de R$ {prestacao_mensal:.2f}") 
else:
    print("Empréstimo negado!")
    print(f"O valor da prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do salário do comprador.")

#prestação mensal tem que ser menor ou igual a 30% do salário do comprador para o empréstimo ser aprovado
#caso contrário, o empréstimo será negado
