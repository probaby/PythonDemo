import re
import requests

url = "http://www.shadowsock.net/index.php#portfolio"
response = requests.get(url)
print(response.text)