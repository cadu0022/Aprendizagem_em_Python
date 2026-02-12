#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('KM: '))
if distancia <= 200:
    print(f'valor percorrido: R${distancia * 0.50}')
else:
    print(f'valor percorrido a cima de 200km: R${distancia * 0.45}')