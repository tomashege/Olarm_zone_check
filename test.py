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

import requests
token = tell_token
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.post(url).json()
print(r)