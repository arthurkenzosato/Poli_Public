import requests

url = "https://argus-adrianodennanni.c9.io:8080/alarm_switch"
payload = {'house_id': '2','active':'1'} 

r = requests.get(url,data=payload)
print(r.url)