import requests

url = f'https://swapi.dev/api/people/'

response = requests.request('GET', url)

print(f'\n{response.text}\n')