import time
import hide
import json
TOKEN = hide.TOKEN
tell_token = hide.tell_token
chat_id = hide.chat_id
# def pushbullet_message(title, body):
#     msg = {"type": "note", "title": title, "body": body}
#     for i in TOKEN:
#         resp = requests.post('https://api.pushbullet.com/v2/pushes', 
#                             data=json.dumps(msg),
#                             headers={'Authorization': 'Bearer ' + i,
#                                     'Content-Type': 'application/json'})
#         if resp.status_code != 200:
#             raise Exception('Error',resp.status_code)
#         else:
#             print ('Message sent') 

# count = 0
# while True:
#     time.sleep(60)
#     pushbullet_message("Test", "HI, this message is still running." + count)
#     count += 1

import requests

url = f'https://api.telegram.org/bot{tell_token}/getUpdates'
out = (requests.post(url).json() )
print(json.dumps(out, indent=4, sort_keys=True))

mess = str(input("We need a message to send to Tomas"))
url = f'https://api.telegram.org/bot{tell_token}/sendMessage'
data = {'chat_id': chat_id, 'text': mess}
requests.post(url, data).json()


def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{tell_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data).json()
