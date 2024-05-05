import requests
import json

update_id = 111111111
update_column = "price"
BASE = f'http://localhost:3000/api/main/kc_house_data/'

data = {
    "id": update_id,
    update_column: "2223333"
}

headers = {'Content-Type': 'application/json'}
response = requests.post(BASE, json=data, headers=headers)


if response.status_code == 200:
    print(response.json())
elif response.status_code == 500:
    print("Internal Server Error. Server response:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")