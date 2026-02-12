#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
#cosseno e tangente desse ângulo.S

import math #biblioteca de matemática

angulo_graus = float(input('digite o angulo em graus:'))
#variavel

#angulo_gradiano = math.radians(angulo_graus) (1° jeito)
radiano = angulo_graus * (math.pi / 180) #transformando o angulo em radiano (2° jeito)

cos = math.cos(radiano) #variavel
sin = math.sin(radiano) #variavel
tan = math.tan(radiano) #variavel

print(f'cos {cos:.2f}')
print(f'sin {sin:.2f}')
print(f'tan {tan:.2f}')

#estudar sen, cos, e tang novamente!
