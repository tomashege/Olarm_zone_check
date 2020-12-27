import hide
headers = hide.headers
import http.client
import mimetypes
import ssl
import json
import time
# mac has some issue with SLL this fixes it 
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

conn = http.client.HTTPSConnection("apiv4.olarm.co")
payload = ''
conn.request("GET", "/api/v4/devices/2731071d-a487-44e8-bb29-fb9a189f6e72/events?pageLength=40", payload, headers)
res = conn.getresponse()
data = res.read()
my_json = data.decode('utf8').replace("'", '"')
jdata = json.loads(my_json)
#s = json.dumps(jdata, indent=4, sort_keys=True)
#print(s)
#print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1609049941457/1000)) )
time_for_active_6 = 0
time_for_active_7 = 0
for i in jdata['data'][::-1]:
    print(time_for_active_7)
    if i['eventNum'] == 6 and i['eventState'] == 'active':
        print("6 - we found an active")
        # get the time from this event... 
        time_for_active_6 = i['eventTime']
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['eventTime']/1000)) )

    if i['eventNum'] == 7 and i['eventState'] == 'active':
        print("7 - we found an active")
        time_for_active_7 = i['eventTime']
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['eventTime']/1000)) )

    if i['eventNum'] == 6 and i['eventState'] == 'closed':
        time_for_active_6 = 0
    if i['eventNum'] == 7 and i['eventState'] == 'closed':
        time_for_active_7 = 0
    
if time_for_active_6 != 0:
    print("we have an open Garaged - 6")
if time_for_active_7 != 0:
    print("we have an open Garaged - 7")



    
    
    





