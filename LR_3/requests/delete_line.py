import requests

delete_id = 111111111
BASE = f'http://localhost:3000/api/main/kc_house_data/{delete_id}'

response = requests.delete(BASE)
print(response.json())