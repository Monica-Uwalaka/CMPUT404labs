import requests

print(requests.__version__)

req = requests.get('https://raw.githubusercontent.com/Monica-Uwalaka/CMPUT404labs/main/script.py')

print(req.text)

