# Shows related artists for the given seed artist
import argparse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get related artists'
                                                 'for the given seed artist')
    parser.add_argument('-a', '--artist', required=True,
                        help='Name of Artist')
    return parser.parse_args()


def main():
    args = get_args()
    result = sp.search(q='artist:' + args.artist, type='artist')

    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)

    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])


if __name__ == '__main__':
    main()
