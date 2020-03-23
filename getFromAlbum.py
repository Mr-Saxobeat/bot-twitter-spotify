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
    albums = sp.current_user_saved_albums()
    for album in albums['items']:
        ab = album['album']
        tracks = ab['tracks']

        for tr in tracks['items']:
            music_name = tr['name']
            music_artist = tr['artists'][0]['name']

            if(music_artist != 'Resgate' and music_artist != 'Cultivo'
                and music_artist != 'King Crimson' and music_artist != 'Os Saltimbancos'
                and music_artist != 'Facada' and music_artist != 'Arrigo Barnabé'
                and music_artist != 'Animals As Leaders' and music_artist != 'Zé Maholics'
                and music_artist != 'Dois Dobrado' and music_artist != 'Black Eyed Peas'):
                print("%s // %s" % (music_name, music_artist))
