import requests
import re

base_url = "http://natas33.natas.labs.overthewire.org/"

s = requests.session()

username = "natas33"
password = "APwWDD3fRAf6226sgBOBaSptGwvXwQhG"


file = open("file.php", "w")
file.write("1,2,3,4")
file.close()

# body="""username=asdf&password='asdf' or 1=1&password=2"""

s = requests.session()
s.get(base_url, auth=(username, password))
res = s.post(base_url, 
             # data=body,
             auth=(username, password), 
             allow_redirects=False)

body = "\n".join(re.findall("<body(.*)</body>", res.text, flags=re.DOTALL)[0].splitlines()[1:])

print("="*80)
print(body)
# print(res.text)
print("="*80)
