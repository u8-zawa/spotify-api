from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


def main():
    auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URI)
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    me = spotify.me()
    pprint(me)


if __name__ == "__main__":
    main()
