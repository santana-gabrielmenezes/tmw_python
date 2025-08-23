#%%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Digite uma palavra: ")
qnt_a = 0

for i in palavra :
    if i.lower() == "a" : qnt_a += 1

print("Esta palavra tem", qnt_a, "letras 'a'!")
# %%