import requests

x = input("Enter your webhook: ")

webhook_url = x

y = input("What do you want me to send: ")
data = {"content": str(y)}

z = input("How many times should i sent it?: ")
z = int(z)

for _ in range(z):
    response = requests.post(webhook_url, json=data)
    print(response.status_code)
