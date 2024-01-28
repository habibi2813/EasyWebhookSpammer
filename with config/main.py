import requests
import json

with open('config.json') as f:
    config = json.load(f)

webhook_url = config["webhook_url"]
data = {"content": config["message"]}
z = int(config["repeat_times"])

for _ in range(z):
    response = requests.post(webhook_url, json=data)
    print(response.status_code)
