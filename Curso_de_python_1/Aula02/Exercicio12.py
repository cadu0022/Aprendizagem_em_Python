#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus_celsius = float(input('digite a temperatura:'))

fahrenheit = (graus_celsius * (9/5)) + 32

print(f'temperatura: {fahrenheit}°f')
