# Sample Program: Web Request

import requests

r1 = requests.get("https://ifconfig.co/json")
print(r1.json())
print("-" * 32)
print("My IP addr:", r1.json()['ip'])
print("My IP location:", "%s, %s, %s"%( r1.json()['city'], r1.json()['country'], r1.json()['country_iso']))
print("My Internet Service Provider:", r1.json()['asn_org'])