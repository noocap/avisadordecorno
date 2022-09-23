import requests



token = '5637147882:AAH0nSsU9jM2655KoagUWO4MUTKmPKMQVOE'
chat_id = '-1001680706416'
mensagem = 'ta chegando a hora corno'
url = f'https://api.telegram.org/bot{token}/sendmessage?chat_id={chat_id}&text={mensagem}'
requests.get(url)