import requests
print('Welcome to the currency converter.')

url = 'https://api.frankfurter.app/latest'


while True:
    first_fiat = input('choose value (usd, eur, etc...): ').upper()
    second_fiat =  input('choose value (usd, eur, etc...): ').upper()

    parametres = {'base': first_fiat, 'to': second_fiat}


    response  = requests.get(url, params=parametres)

    if response.status_code == 200:
        data = response.json()
        final = data['rates'][second_fiat]
        print(f'1 {first_fiat} = {final} {second_fiat}')

    else:
        print(f'Sorry, {first_fiat} or {second_fiat} unsupported currency!')
        print(str(response.status_code) + ' Error')
