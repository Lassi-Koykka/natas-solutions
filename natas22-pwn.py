import requests, html

base_url = "http://natas22.natas.labs.overthewire.org/"
source_url = base_url + "index-source.html"

s = requests.session()

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

res1 = s.get(source_url, auth=(username, password))

print(html.unescape(res1.text))
print("="*80)
sessid = res1.cookies["PHPSESSID"]
print(sessid)
print("="*80)
