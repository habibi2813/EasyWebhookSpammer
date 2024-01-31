import requests
import json
import threading

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    return config

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def send_request(webhook, message):
    response = requests.post(webhook, json={"content": message})
    print(response.status_code)

def main():
    config = load_config()

    x = input("Enter your webhook (or press Enter to use the last one): ")
    if x:
        config['webhook'] = x

    y = input("What do you want me to send (or press Enter to use the last one): ")
    if y:
        config['message'] = y

    z = input("How many times should I send it (or press Enter to use the last one)? ")
    if z:
        config['times'] = z

    save_config(config)

    threads = []
    for _ in range(int(config.get('times'))):
        t = threading.Thread(target=send_request, args=(config.get('webhook'), config.get('message')))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
