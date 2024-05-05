import requests
year = 2014
month = 10
BASE = f'http://localhost:3000/api/main/kc_house_data/{year}/{month}/'

response = requests.get(BASE)
if response.status_code == 200:
    print(response.json())
elif response.status_code == 500:
    print("Internal Server Error. Server response:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")