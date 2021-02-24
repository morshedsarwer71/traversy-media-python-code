import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
j=r.json()
del j['id']
print(j)