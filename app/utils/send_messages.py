import requests
import json
import os

def SendMessageWhatsapp(data):
    try:
        token = os.environ.get("TOKEN")
        api_url= "https://graph.facebook.com/v15.0/109499142068659/messages"
        headers = {"Content-Type": "application/json", "Authorization":f"Bearer {token}"}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print(True)
            return True
        return False
    except Exception as e:
        print(e)
        return False
