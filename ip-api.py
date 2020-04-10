#!/usr/bin/env python3

import requests
import json
import sys

query = input('Enter ip addr to get info about: ')

url = f'http://ip-api.com/json/{query}?fields='

funcs = ['continent','continentCode','country',\
        'countryCode','region','regionName','city','district','zip',\
        'lat','lon','timezone','currency','isp','org','as','asname',\
        'reverse','mobile','proxy','hosting','all']

for func in funcs:
    print(str(funcs.index(func)+1)+'.) '+func)

choices = []
k = 0

for choice in input('Enter choice (eg.1,2,3): ').split(','):
    try:
        ch = int(choice)
    except:
        print('Enter a valid input!')
        sys.exit(0)
    if funcs[ch-1] == 'all':
        url = f'http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'
        k = 1
        break
    else:
        choices.append(ch)


if not k==1:
    for choice in choices:
        url += funcs[choice-1]+','
    url += 'query,status,message'

resps = json.loads(requests.get(url).text)
print()

for resp in resps:
    print(f'\t{resp}: {resps[resp]}')
