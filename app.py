import requests

API_KEY = '0b1ea1b8927ce0b7dcad7e38daa4cb8a'  
CIDADE = 'Goiânia,BR'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CIDADE}&appid={API_KEY}&units=metric'

def checar_previsao_chuva():
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            print(f'Previsão do tempo para os próximos dias em Goiânia:')
            for item in data['list']:
                dt_txt = item['dt_txt']  
                clima = item['weather'][0]['description']
                print(f'{dt_txt}: {clima}')

                if 'chuva' in clima.lower():
                    print('Aviso: Vai chover!')
                else:
                    print('Não há previsão de chuva.')
        else:
            print(f'Erro na requisição: {data["message"]} (Código: {response.status_code})')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == "__main__":
    checar_previsao_chuva()
