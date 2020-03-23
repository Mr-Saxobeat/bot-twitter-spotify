import spotipy
import spotipy.util as util
from decouple import config

username = config('SPOTIPY_USER_ID')
scope = 'user-library-read'
SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)


        sp = spotipy.Spotify(auth=token)
