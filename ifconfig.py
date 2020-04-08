#!/usr/bin/env python3

import requests

url = 'https://ifconfig.me/'

funcs = ['ip', 'host', 'ua', 'port', 'lang', 'via', 'forwarded', 'all']

print('Choose :')

for func in funcs:
    print(str(funcs.index(func)+1)+'.) '+func)

ch = int(input('Enter a choice: '))

furl = url+funcs[ch-1]

r = requests.get(furl)

print()
print(f'{funcs[ch-1]}:\n\n{r.text}')
