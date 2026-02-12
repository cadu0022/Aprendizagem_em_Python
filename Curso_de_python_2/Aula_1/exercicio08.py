#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo
#Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc >= 18.5 and imc < 25:
    print("Status: Peso Ideal")
elif imc >= 25 and imc < 30:
    print("Status: Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Status: Obesidade")
elif imc >= 40:
    print("Status: Obesidade Mórbida")