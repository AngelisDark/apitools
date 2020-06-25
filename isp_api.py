import requests
import json

phone = input('Enter phone number : ')

url = f'https://digitalapiproxy.paytm.com/v1/mobile/getopcirclebyrange?channel=web&version=2&number={phone}&child_site_id=1&site_id=1&locale=en-in'

headers = {
    'Host': 'digitalapiproxy.paytm.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://paytm.com/',
    'Origin': 'https://paytm.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

r = json.loads(requests.get(url, headers=headers).text)

if r['status'] == True:

    print("\n\tOperator :", r['Operator'])
    print('\tCircle :', r['Circle'])

    if r['postpaid'] == False:
        print('\tType : prepaid')
    else:
        print('\tType : postpaid')
