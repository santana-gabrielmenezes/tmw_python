#%%
# Faça um programa que verifique se o item que a pessoa escolheu para comprar
# na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

lista = "laranja, cerveja, miojo, carvão, picanha"
produto = input("Digite seu nome do produto: ")

if produto.lower() in lista :
    print("o produto ta na lista")
else : print("o produto não está na lista")
# %%
