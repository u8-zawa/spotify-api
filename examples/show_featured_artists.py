# Shows all artists featured on an album
import argparse
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get all artists featured on an album')
    parser.add_argument('-a', '--aid', required=True,
                        help='Album id')
    return parser.parse_args()


def main():
    args = get_args()
    album = sp.album(args.aid)

    featured_artists = set()

    items = album['tracks']['items']

    for item in items:
        for ele in item['artists']:
            if 'name' in ele:
                featured_artists.add(ele['name'])

    pprint(featured_artists)


if __name__ == '__main__':
    main()
