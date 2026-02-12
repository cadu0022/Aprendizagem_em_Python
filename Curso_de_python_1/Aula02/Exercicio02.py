#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

#usei o copilot para entender pouco de como usar de fato o if e do else.
#if o else e o elif são estruturas condicionais, que estou aprendendo na faculdade, por isso usei.

n = input('digite algo: ')
#verifica o tipo primitivo

print('é alfanumérico?', n.isalnum())
print('é alfabético?', n.isalpha())
print('é decimal?', n.isdecimal())
print('Tem espaços?', n.isspace())
print('Esta tudo minusculo?', n.islower())
print('Esta tudo maiusculo?', n.isupper())
print('Esta capitalizada?', n.istitle())

# Tenta converter para int , caso for numero, caso n for numero,
#  ele n faz a conversão e mostra o tipo original

if n.isnumeric(): #se for numero vai da true
    n = int(n)
    print('convertido para int', type(n))

else: #se n for numero, vai da false
    print('tipo original', type(n))


