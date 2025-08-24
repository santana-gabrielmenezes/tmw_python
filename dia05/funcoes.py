# y = f(x) = x + 10
# y= f(x) = x^2 + 1
#%%

# definição da função
def funcao(x) :
    res = x + 10
    return res

# %%

# invocação da função
y = funcao(10)
print(y)

# %%

def soma (a,b=0) :
    return a + b

#%%

soma(10,20)
# %%

soma(10)

# %%

soma(a=10,b=20)

# %%

soma(b=20,a=10)

# %%

soma(b=20)