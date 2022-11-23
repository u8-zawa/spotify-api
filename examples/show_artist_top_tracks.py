# Shows artist info for a URN or URL
import argparse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get Spotify catalog information'
                                                 'about an artist’s top 10 tracks by country..')
    parser.add_argument('-a', '--artist', required=True,
                        help='Name of Artist')
    return parser.parse_args()


def main():
    args = get_args()
    results = sp.artist_top_tracks(args.artist)
    for track in results['tracks']:
        print(track['name'])


if __name__ == '__main__':
    main()
