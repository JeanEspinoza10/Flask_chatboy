import requests
import json
import os

def SendMessageWhatsapp(data):
    try:
        token = os.environ.get("TOKEN")
        api_url= os.environ.get("API_URL")
        headers = {"Content-Type": "application/json", "Authorization":f"Bearer {token}"}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print(True)
            return True
        return False
    except Exception as e:
        print(e)
        return False
