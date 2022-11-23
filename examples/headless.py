import spotipy

from spotipy.oauth2 import SpotifyOAuth

from utils import spotify

# set open_browser=False to prevent Spotipy from attempting to open the default browser
auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                            client_secret=spotify.CLIENT_SECRET,
                            redirect_uri=spotify.REDIRECT_URI,
                            open_browser=False)
sp = spotipy.Spotify(auth_manager=auth_manager)

print(sp.me())
