#%%
# Faça um programa que verifique se a pessoa pertence à família "Calvo" ou "Silva"

nome_completo = input("Digite seu nome completo: ")

if "Calvo" in nome_completo.lower() or "Silva" in nome_completo.lower() :
    print("É da família!")
else : print("Não é da família!")
# %%
