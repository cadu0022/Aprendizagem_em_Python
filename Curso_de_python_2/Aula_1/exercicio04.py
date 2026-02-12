#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime # From datetime importa a classe datetime. ou seja importando apenas a classe datetime da biblioteca datetime
data_nascimento_str = input("Digite a data: ") # digita a data no formato ddmmyyyy -> string para o usuario relacionada a data

data = datetime.strptime(data_nascimento_str,"%d%m%Y") #converte a string para o formato de data
print(data.strftime("%d/%m/%Y")) # strftime formatação da data para o formato objeto que é a data -> string parse data


ano_nascimento = data # obtém o ano de nascimento a partir da data fornecida
ano_atual = datetime.now().year #datatime.now pega a data atual e .year pega o ano atual
idade = ano_atual - ano_nascimento.year # calculos da idade, subtraindo o ano atual pelo ano de nascimento 
tempo_para_alistamento = 18 - idade # calcula o tempo para o alistamento. calucula 18 que é a idade do alistamento - idade do usuario
print(f"Quem nasceu em {ano_nascimento.year} tem {idade} anos em {ano_atual}.") # mostra ao usuario a data de nascimento formatada e a idade atual

if idade < 18: # verifica condição se a idade é menor que 18 -> se for verdade executa o bloco de código, se for falsa pula para o próximo bloco
    print(f"Ainda faltam {tempo_para_alistamento} anos para o alistamento.") # mostra ao usuario o tempo que falta para o alistamento
    ano_do_alistamento = ano_atual + tempo_para_alistamento # calcula o ano do alistamento = ano atual + com o tempo que falta para o alistamento
    print(f"O alistamento será em {ano_do_alistamento}.") # mostra ao usuario o ano do alistamento

elif idade == 18: # verifica condição se a idade é igual a 18 -> se for verdade executa o bloco de código, caso for falsa pula para o próximo bloco
    print("Comparecer a uma junta de serviço militar.") # mostra ao usuario a mensagem para comparecer a junta de serviço militar, caso a idade seja 18 anos

else: # se nenhuma das condições anteriores forem verdadeiras, executa o bloco de código
    anos_passados = idade - 18 # calcula os anos passados do alistamento = idade - 18
    print(f"Já se passaram {anos_passados} anos do prazo de alistamento.") # mostra ao usuario os anos que já passaram do prazo de alistamento
    ano_do_alistamento = ano_atual - anos_passados # calcula o ano do alistamento = ano atual - anos que já passaram do prazo de alistamento
    print(f"O alistamento foi em {ano_do_alistamento}.") # mostra ao usuario o ano do alistamento
    print("Procure a junta militar mais próxima.") # mostra ao usuario a mensagem para procurar a junta militar mais próxima