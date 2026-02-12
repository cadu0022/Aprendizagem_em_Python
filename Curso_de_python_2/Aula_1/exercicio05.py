#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida

print("Cálculo de Média Escolar")
print('-'*50)
print('O trabalho vale 3 ponto.')
print('A prova vale 10 pontos.')

v1 = float(input("V1: "))
v2 = float(input("V2: "))
trabalho = int(input("Trabalho: "))
print('-'*50)
prova = v1 + v2
media = (prova + trabalho) / 2

if media > 6 :
    print(f"A média do aluno é {media:.2f}. Aluno aprovado.")
elif media == 6 :
    print(f"A média do aluno é {media:.2f}. Aluno aprovado.")
elif media < 6 :
    print(f"A média do aluno é {media:.2f}. Aluno recuperação.")
    print('-'*50)
    recuperacao = int(input("Prova de recuperação: "))
    if recuperacao >= 6 :
        print(f"sua nota é {recuperacao}. Aluno aprovado.")
    else :
        print(f"sua nota é {recuperacao}. Aluno reprovado.")
else :
    print("Erro, tente novamente.")
