#%%

# faça um programa que receba 4 alturas

count = 1
alturas = []
altura = ''
soma_alturas = 0

while count <= 4 :
    print('entre com a ',count,'° altura: ')
    altura = float(input())
    alturas.append(altura)
    count += 1

soma_alturas = sum(alturas)

print('a soma das alturas é: ',soma_alturas)
# %%

