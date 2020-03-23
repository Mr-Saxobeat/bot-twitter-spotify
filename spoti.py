import sys
import spotipy
import spotipy.util as util
from decouple import config


if len(sys.argv) > 1:
    scope = 'user-library-read'
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope,
        client_id=config('SPOTIPY_CLIENT_ID'), client_secret=config('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=config('SPOTIPY_REDIRECT_URI'))

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
