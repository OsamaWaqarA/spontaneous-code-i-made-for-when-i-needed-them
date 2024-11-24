import requests

app_id = "4217b516c6774491876594af3598339e"
from_currency = 'SAR'
to_currency = 'PKR'
amount = 2000

url = f'https://openexchangerates.org/api/latest.json?app_id={app_id}&symbols={from_currency},{to_currency}'

response = requests.get(url)
#print(response.status_code)  # Print the HTTP status code
#print(response.json())  # Print the JSON response

data = response.json()
exchange_rate = data['rates'][to_currency] / data['rates'][from_currency]

result = amount * exchange_rate

print(f'{amount} {from_currency} is equal to {result:.2f} {to_currency}')

print(result)
