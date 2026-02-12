from random import randint
from time import sleep

velocidade = randint(0,200)
multa = (velocidade - 80) * 7

print('--'*15)
print('Radar eletrônico'.center(30))
print('--'*15)
sleep(2)
if velocidade < 80:
    print('boa viagem! dirija com segurança')
else:
    print(f'Velocidade registrada: {velocidade}km/h')
    print(f'Excesso de velocidade: {velocidade - 80}km/h')
    print(f'Você foi multado em: R${multa}')

