python 
import requests
url = 'https://api.githup.com/user'
response = requests.get(url)
response.json()
response = requests.get(url,auth = ('userName','password')
response.json()
response = requests.get(url,headers = {'Authorization':'Bearer Your Access Tokens'})
response.json()