import time
import hide
TOKEN = hide.TOKEN
def pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent') 
count = 0
while True:
    time.sleep(60)
    pushbullet_message("Test", "HI, this message is still running." + count)
    count += 1