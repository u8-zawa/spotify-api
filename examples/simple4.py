from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify


def main():
    auth_manager = SpotifyOAuth(client_id=spotify.CLIENT_ID,
                                client_secret=spotify.CLIENT_SECRET,
                                redirect_uri=spotify.REDIRECT_URI)
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    me = spotify.me()
    pprint(me)


if __name__ == "__main__":
    main()
