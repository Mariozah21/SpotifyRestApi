from re import template
import requests
import base64
import json


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
    return token
#authorized token
authToken = generateAccessToken(ClientID,ClientPassword)

#Query url
url = "https://api.spotify.com/v1/artists/53XhwfbYqKCa1cC15pYq2q/top-tracks"
querystring = {"market":"CZ"}

headers = {
    "accept": "application/json"
    ,"Authorization": f"Bearer {authToken}"
}
#raw data from query
response = requests.request("GET", url, headers=headers, params=querystring)
#extraction of data
tracks=[]
for track in response.json()['tracks']:
    tlseconds,tlmiliseconds = divmod(track['duration_ms'],1000)
    tlminutes,tlseconds = divmod(tlseconds,60)
    if tlseconds<10:
        tlseconds=("0"+str(tlseconds))
    else:
        tlseconds=str(tlseconds)

    trackLength = ( str(tlminutes) + ":"+ tlseconds)
    trackinfo=dict(name=str(track['name']),id=str(track['id']),popularity=str(track['popularity']),album=str(track['album']['name']),length=trackLength)
    tracks.append(trackinfo)

         

    