import sys
import spotipy
import spotipy.util as util
from decouple import config

username = config('SPOTIPY_USER_ID')
scope = 'user-library-read'
SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("%s // %s" % (track['name'], track['artists'][0]['name']))

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            results = sp.playlist(playlist['id'],
            fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
        elif(playlist['name'] == 'On Repeat' or playlist['name'] == 'Repeat Rewind'
            or playlist['name'] == 'Your Top Songs 2019' or playlist['name'] == 'Your Top Songs 2018'
            or playlist['name'] == 'Your Top Songs 2017' or playlist['name'] == 'Your Top Songs 2016'):
            results = sp.playlist(playlist['id'],
                fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
