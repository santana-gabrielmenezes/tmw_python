#%%

dados = ['teo','calvo',31]

nome = dados[0]

#%%

dados = {
    'nome' : 'teo',
    'sobrenome' : 'calvo',
    'idade' : 31,
    'exs' : ['nah','josefina','elaine'],
    'filhos' : [{
        'nome' : 'maria',
        'idade' : 2
        },{
        'nome' : 'raul',
        'idade' : 1
        }]
}

print(dados['filhos'][0]['idade'])
# %%
