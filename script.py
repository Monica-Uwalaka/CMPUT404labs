import requests

print(requests.__version__)

req = requests.get('https://www.google.com')

print(req.text)