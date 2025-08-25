#%%

import requests

url = "http://api.opendota.com/api/heroes"

resposta = requests.get(url)

#%%

resposta.status_code
# %%

dados = resposta.json()
# %%

dados[0]['localized_name']

#%% 

