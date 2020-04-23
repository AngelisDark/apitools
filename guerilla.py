import requests
import json

url = 'http://api.guerrillamail.com/ajax.php'

def get_email_address():
    data = {
        'f': 'get_email_address'
    }

    r = requests.get(url,params=data)
    resp = json.loads(r.text)

    print(f"""
        Your Email Address:  {resp['email_addr']}
        Your SID Token:      {resp["sid_token"]}
        """)



get_email_address()
