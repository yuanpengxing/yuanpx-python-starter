# -*- coding: UTF-8 -*-
import requests

data = '{"callbackType":"1","callbackUri":"http://121.36.111.187:44597/VM-ALARM/alarm/receive/receiveAlarm","channelId":"5","endSubsTime":"1593532800000","resourceType":35,"isValid":true}'
header = {"Content-Type": "application/json;charset=utf-8"}
try:
    result = requests.post("https://117.78.52.95:443/vas/api/v2/info/subscribe", data, headers=header, verify=False)
except Exception as e:
    print("Exception")

print(result.text)
