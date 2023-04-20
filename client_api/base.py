import requests

endpoint = 'http://127.0.0.1:8000/api'

reponse = requests.post(endpoint)
print (reponse.json())
print (reponse.status_code)