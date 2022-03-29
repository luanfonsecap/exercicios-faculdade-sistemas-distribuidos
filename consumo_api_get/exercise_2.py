import requests

url = 'https://viacep.com.br/ws/'
zipcodes = ['30140071', '30140072', '30140073', '30140074', '30140075']
formato = '/json/'

for zipcode in zipcodes:
    r = requests.get(url + zipcode + formato)

    if (r.status_code == 200):
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Nao houve sucesso na requisição.')
