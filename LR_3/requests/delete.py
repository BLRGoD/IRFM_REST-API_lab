import requests

BASE = 'http://localhost:3000/api/main/kc_house_data/'

response = requests.delete(BASE + '7129300520')
print(response.json())