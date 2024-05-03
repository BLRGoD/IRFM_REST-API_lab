import requests

line_id = 7129300520
BASE = f'http://localhost:3000/api/main/kc_house_data/{line_id}'

response = requests.get(BASE)
print(response.json())