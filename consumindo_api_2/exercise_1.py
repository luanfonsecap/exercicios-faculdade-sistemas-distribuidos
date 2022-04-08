import requests
import sqlite3


def currency(value):
    if response.status_code == 200:

        responseConvertedToJson = response.json()

        print('Valor em Dollar:')
        dollar = value / (responseConvertedToJson['results']['currencies']['USD']['buy'])
        print(round(dollar, 2))

        print('Valor em Euro:')
        euro = value / (responseConvertedToJson['results']['currencies']['EUR']['buy'])
        print(round(euro, 2))

        print("Data da consulta:")
        dates = (responseConvertedToJson['results']['taxes'][0]['date'])

        print(dates)
    

        cur.execute(
            "INSERT INTO cotacoes VALUES (null,?,?,?)", (round(dollar, 2), round(euro, 2), dates))

        con.commit()

    else:
        print('Ocorreu um erro ao buscar dados')


if __name__ == '__main__':

    con = sqlite3.connect('cotacoes.db')

    cur = con.cursor()

    url = 'https://api.hgbrasil.com/finance?format=json-cors&key=be673517 '

    response = requests.get(url)

    value = float(input('Digite o valor a ser convertido: '))

    currency(value)

