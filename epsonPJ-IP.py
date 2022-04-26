#!/usr/bin/python3
#For TW7100 with ELPAP10 (likely works on TW7000 also)
#Heavily adapted and credit to https://gist.github.com/0x4C4A/645b7a97281d624d88e29fcd7330fd75 and https://www.avsforum.com/threads/official-epson-5040ub-6040ub-owners-threa>

import requests
import re
import time
import sys

projectorAddress = 'http://192.168.1.47'
username = 'EPSONMOBILE'
password = ''

auth = requests.auth.HTTPBasicAuth(username, password)
headers= {'Referer': projectorAddress + '/mobile/index.html?EPSON=Projector'}
page = {'page': '901'}

def getRequest(url):
  return requests.get(projectorAddress + url, auth = auth, headers = headers)

def projectorIsOn():
  r = requests.post(projectorAddress + '/cgi-bin/webconf', data = page, auth = auth,
                       headers = headers)
  retval = r.text.find('The projector is currently on standby.</p>') == -1
  return retval

def turnProjectorOn():
  if not projectorIsOn():
    getRequest('/cgi-bin/directsend?KEY=3B')
    time.sleep(0.3)

def turnProjectorOff():
  if projectorIsOn():
    getRequest('/cgi-bin/directsend?KEY=3B')
    time.sleep(0.3)
    getRequest('/cgi-bin/directsend?KEY=3B')

def ProjectorStatus():
  if projectorIsOn():
    print('Projector is on')
  if not projectorIsOn():
    print('Projector is off')

argument = sys.argv[1] or ''
if sys.argv[1] == 'on':
  turnProjectorOn()
elif sys.argv[1] == 'off':
  turnProjectorOff()
elif sys.argv[1] == 'status':
  ProjectorStatus()
else:
  print("Run script with parameter 'on' or 'off' or 'status'")
  sys.exit(1)

