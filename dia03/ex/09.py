#%%
# Faça um programa que receba uma quantidade indefinida de valores
# correspondentes a “saldo em conta”, mas quando o usuário apertar
# “enter” sem digitar valor algum, o programa para de receber valores,
# e exibe a soma te todos os valores digitados anteriormente.

entrada = input("Digite o valor: ")
total = 0

while True :
    if entrada == "" :
        break
    else :
        total += float(entrada)
        entrada = input("Digite o prócimo valor: ")

print("O valor da soma é ", total)
# %%
