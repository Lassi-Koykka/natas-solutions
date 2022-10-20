import requests, html
cookieData = "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"


base_url = "http://natas11.natas.labs.overthewire.org/"
source_url = base_url + "index-source.html"

s = requests.session()

username = "natas11"
password = "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"

res1 = s.get(base_url, auth=(username, password), cookies={'data': cookieData})

print(html.unescape(res1.text))
print("="*80)
# sessid = res1.cookies["PHPSESSID"]
# print(sessid)
print("="*80)
