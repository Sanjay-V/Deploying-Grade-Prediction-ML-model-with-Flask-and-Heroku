import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Language 1': 12, 'Language 2': 45, 'Math': 32, 'Science': 34, 'Computer Science': 21})

print(r.json())