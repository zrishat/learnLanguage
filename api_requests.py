import requests

# доступно без авторизации
url = 'http://127.0.0.1:8000/drf/groups'
response = requests.get(url)
print('доступно без авторизации ', response.status_code)

# недоступно без авторизации
url = 'http://127.0.0.1:8000/drf/users/'
response = requests.get(url)
print('недоступно без авторизации ', response.status_code)

# доступно с авторизацией (Базовая авторизация)
url = 'http://127.0.0.1:8000/drf/users/'
response = requests.get(url, auth=('admin', 'admin'))
print("доступно с авторизацией ", response.status_code)

# доступно с авторизацией (Токен авторизация)
data = {
    'username': 'admin',
    'password': 'admin'
}
response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
token = response.json()['token']
url = 'http://127.0.0.1:8000/drf/users/'
headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
print("доступно с авторизацией по токену", response.status_code)
