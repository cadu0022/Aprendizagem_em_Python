#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

a_altura = float(input('digite um valor: '))
b_largura= float(input('digite um valor: '))

area = a_altura * b_largura 
litro_necessarios = area / 2

print(f'area {area}²')
print(f'{litro_necessarios:.2f}L')