import requests
import base64
import json
#from secrets import *

ClientID = "1855ccc24e144ff4a8daef9848c4780f"
ClientPassword = "2a001b3e61894450ad7ae6bc763477a1"

# Autorization
Authurl = 'https://accounts.spotify.com/api/token'
headers = {}
data = {}


def generateAccessToken(ClientId,ClientSecret):
    # Encode 
    message = f"{ClientId}:{ClientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(Authurl, headers=headers, data=data)

    token = r.json()['access_token']
    print(r.json())
    return token

authToken = generateAccessToken(ClientID,ClientPassword)


    