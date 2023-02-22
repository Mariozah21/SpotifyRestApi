import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '1855ccc24e144ff4a8daef9848c4780f'
secret = '2a001b3e61894450ad7ae6bc763477a1'

client_credentials_manager = SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)