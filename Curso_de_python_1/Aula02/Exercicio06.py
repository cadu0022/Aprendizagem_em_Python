#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# 1cm = 10mm
# 100cm = 1000mm
# 1m = 100cm

metros = float(input('Digite um valor em metros: '))

centimetros = metros * 100 # 1m = 100cm 
milimetros = metros * 1000 # 1m = 100cm = 1000mm

print(f'{metros} metros equivalem a {centimetros} centímetros e {milimetros} milímetros.')
