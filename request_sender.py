import requests

def send_event(event, data):
    url = "http://localhost:3000/bot-events"
    payload = {
        "event": event,
        "data": data
    }

    try:
        response = requests.post(url, json=payload)
        
        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            print(f"POST request successful. Status code: {response.status_code}")
        else:
            print(f"POST request failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")