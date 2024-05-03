import requests
import json

new_id = 111111111
BASE = f'http://localhost:3000/api/main/kc_house_data/'

data = {
    "id": new_id,
    "date": "20141013T000000",
    "price": 221900,
    "yr_built": 1960,
    "yr_renovated": 0,
    "sqft_living": 1180,
    "condition": 3,
    "real_year": 2027
}

headers = {'Content-Type': 'application/json'}
response = requests.post(BASE, json=data, headers=headers)
# print(response.json())
if response.status_code == 200:
    print(response.json())
elif response.status_code == 500:
    print("Internal Server Error. Server response:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")