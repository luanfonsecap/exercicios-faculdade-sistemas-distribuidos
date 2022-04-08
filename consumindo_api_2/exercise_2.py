import requests


def tempo(cidade_estado):
    url = (
        f'https://api.hgbrasil.com/weather?key=807bcfaf&city_name={cidade_estado}')

    resposta = requests.get(url)

    if resposta.status_code == 200:
        json = resposta.json()

        cidade = (json['results']['city'])
        tempo = (json['results']['temp'])
        data = (json['results']['date'])
        hora = (json['results']['time'])
        descrip = (json['results']['description'])
        turno = (json['results']['currently'])
        umidade = (json['results']['humidity'])
        vento = (json['results']['wind_speedy'])
        nascersol = (json['results']['sunrise'])
        porsol = (json['results']['sunset'])
        condtempo = (json['results']['condition_slug'])

        print(f'Cidade: {cidade}')
        print(f'Temperatura atual: {tempo}')
        print(f'Data e Hora da consulta: {data} {hora}')
        print(f'Descrição do tempo atual: {descrip}')
        print(f'Turno: {turno}')
        print(f'Umidade: {umidade}')
        print(f'Velocidade do vento: {vento}')
        print(f'Nascer do sol: {nascersol}')
        print(f'Pôr do sol: {porsol}')
        print(f'Condição de tempo atual: {condtempo}')
        print(f'Médias das temperaturas máxima e mínima da semana: ')
        semana_min = 0
        semana_max = 0
        for dia in range(1, 8):

            semana_min += (json['results']['forecast'][dia]['min'])
            semana_max += (json['results']['forecast'][dia]['max'])

        print('Min: ')
        print(round(semana_min/7, 2))
        print('Max: ')
        print(round(semana_max/7, 2))

    else:
        print('Falhou')


if __name__ == '__main__':

    cidade_estado = input('Digite a cidade e estado: ')
    tempo(cidade_estado)
