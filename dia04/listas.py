#%%

# criando uma lista
minha_lista = []
print(minha_lista)

#%%

#atribuido valor a uma lista
minha_lista = ['teo','calvo',31,1.82]
print(minha_lista)

#%%

# acessando o primeiro valor da lista
minha_lista[0]

#%%

# acessando o segundo valor da lista
minha_lista[1]
#%%

# acessando ultimo valor (primeiro do final para o começo) da lista
minha_lista[-1]

#%%

# acessando os dois primeiros elementos
minha_lista[:2]

#%%

# acessando os dois ultimos elementos da lista
minha_lista[:-2]

# %%

# criando uma nova lista com os mesmos elementos da orimeira
nova_lista = minha_lista[:]
print(nova_lista)

# %%

# usando o step para definir os saltos entre um elemento e outro, neste caso um elemento no sentido de trás para frente
minha_lista[::2]

# %%

# usando o step para inverter a lista
minha_lista[::-1]

#%%

notas = []
nota = 7.5

notas.append(nota)
print(notas)

notas.append(10)
print(notas)

notas.extend([5.75,6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)

# %%

nomes = ['teo','maria','nah']
for nome in nomes :
    print(nome.title())

nomes.extend(['jose','lila'])

print(nomes)

# %%

nomes.extend('teodoro')

print(nomes)
# %%

nomes.append('teodoro')

print(nomes)
# %%

dados = ['teo','calvo',31,['nah','josefina','elaina'],['mariana']]

exs = dados[3]
ex_1 = exs[-1]

#%%

dados[-1][0][0]
# %%
