#!/usr/bin/env python3

#Find my dns provider

import requests
import json

url = 'http://edns.ip-api.com/json'

r = requests.get(url)

resp = json.loads(r.text)["dns"]

print(f'Your DNS Provider is {resp["geo"]}\nYour IP address is {resp["ip"]}')
