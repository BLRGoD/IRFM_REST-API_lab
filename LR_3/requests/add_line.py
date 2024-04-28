import requests

BASE = 'http://localhost:3000/api/main/kc_house_data/'

response = requests.post(BASE, {"date":"20141013T000000","price":221900,"bedrooms":3,"bathrooms":1,
"sqft_living":1180,"sqft_lot":5650,"floors":1,"waterfront":0,"view":0,"condition":3,"grade":7,"sqft_above":1180,
"sqft_basement":0,"yr_built":1955,"yr_renovated":0,"zipcode":"98178","lat":47.5112,"long":-122.257,"sqft_living15":1340,
"sqft_lot15":5650})

print(response.json())