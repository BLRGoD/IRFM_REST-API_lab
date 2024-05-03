import requests

delete_id = 1954400510
BASE = f'http://localhost:3000/api/main/kc_house_data/{delete_id}'

response = requests.delete(BASE)
print(response.json())