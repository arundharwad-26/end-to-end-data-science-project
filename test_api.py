import requests

url = "http://127.0.0.1:5000"

data = {
    "hours": 6,
    "attendance": 85,
    "previous_score": 70
}

response = requests.post(url, json=data)

print(response.json())