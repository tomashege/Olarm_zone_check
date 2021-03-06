import hide
headers = hide.headers
TOKEN = hide.TOKEN
tell_token = hide.tell_token
chat_id = hide.chat_id
import http.client
import mimetypes
import ssl
import json
import time
from time import localtime, strftime
from datetime import datetime
import requests
import json

# mac has some issue with SLL this fixes it 
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def send_to_telegram(message):
    url = 'https://api.telegram.org/bot'+tell_token+'/sendMessage'
    for i in chat_id:
        data = {'chat_id': i, 'text': message}
        try:
            requests.post(url, data).json()
            print("Message sent to Telegram")
        except:
            print("message did not send")

print("start")
send_to_telegram("Start - The code has started")

time_for_active_6 = 0
time_for_active_7 = 0
while True:
    try:
        conn = http.client.HTTPSConnection("apiv4.olarm.co")
        payload = ''
        conn.request("GET", "/api/v4/devices/2731071d-a487-44e8-bb29-fb9a189f6e72/events?pageLength=40", payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        my_json = data.decode('utf8').replace("'", '"')
        jdata = json.loads(my_json)
        for i in jdata['data'][::-1]:
            if i['eventNum'] == 6 and i['eventState'] == 'active':
                time_for_active_6 = i['eventTime']

            if i['eventNum'] == 7 and i['eventState'] == 'active':
                time_for_active_7 = i['eventTime']

            if i['eventNum'] == 6 and i['eventState'] == 'closed':
                time_for_active_6 = 0
            if i['eventNum'] == 7 and i['eventState'] == 'closed':
                time_for_active_7 = 0
        # Function to find the diffrence between two dates.    
        def time_between(d1, d2):
            d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
            d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
            #return d2-d1
            return abs((d2 - d1).seconds/60)

        if time_for_active_6 != 0:
            time_from_the_gararge = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_for_active_6/1000)))
            current = ( strftime("%Y-%m-%d %H:%M:%S", localtime() ) )
            elapsed = time_between(time_from_the_gararge, current)
            if  elapsed > 10:
                print("The Gararge (orange car) has been open for longer then ",elapsed , "mins" )
                send_to_telegram("The door (orange car) has been open for " + str(elapsed) + " mins")
                time.sleep(120)

        if time_for_active_7 != 0:
            time_from_the_gararge = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_for_active_7/1000)))
            current = ( strftime("%Y-%m-%d %H:%M:%S", localtime() ) )
            elapsed = time_between(time_from_the_gararge, current)
            if  elapsed > 10:
                print("the Gararge (blue car) has been open for longer then ",elapsed , "mins" )
                send_to_telegram("The door (blue car) has been open for " + str(elapsed) + " mins")
                time.sleep(120)
        # finaly we wait for 2 mins and then we do the whole process again
        time.sleep(120)
    except:
        print("An error occurred try again")
        try:
            send_to_telegram("ERROR - Somthing went wrong - check the terminal")
        except:
            print("push bullet / telei is not working")
        time.sleep(10)