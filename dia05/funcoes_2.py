#%%

def operacao(op,*num) :

    if op == 'soma' :
        total = 0
        for i in num :
            total += i
    elif op == 'mult' :
        total = 1
        for i in num :
            total = total * i
    return total

operacao('mult', 1,2,3,4)
# %%

dados = ['teo','calvo',31,['nah','elaine','josefina']]

nome, sobrenome, *_, exs = dados

print(nome)
print(sobrenome)
print(exs)
# %%

# inverter valores de variáveis em outras linguagens de programação
a = 10
b = 20
print(a , b)

c = a
a = b
b = c
print(a , b)

# inverter valores de variáveis em outras linguagens de programação
a = 10
b = 20
print(a , b)

a,b = b,a
print(a , b)
# %%
