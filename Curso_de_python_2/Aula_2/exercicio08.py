#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
texto_junto = "".join(palavras)

texto_invertido = ""

for letra in range(len(texto_junto) - 1, -1, -1):
    texto_invertido += texto_junto[letra]
    # Se o print estiver aqui (com espaços atrás), ele imprime letra por letra.

# O print deve ficar aqui, colado na borda esquerda:
print(f"O inverso de {texto_junto} é {texto_invertido}")

if texto_invertido == texto_junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo.")