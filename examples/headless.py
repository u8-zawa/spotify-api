import spotipy

from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

# set open_browser=False to prevent Spotipy from attempting to open the default browser
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            open_browser=False)
sp = spotipy.Spotify(auth_manager=auth_manager)

print(sp.me())
