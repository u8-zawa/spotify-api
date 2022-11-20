# Shows album info for a URN or URL
import argparse
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from settings import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get single album.')
    parser.add_argument('-a', '--aid', required=True,
                        help='Album id')
    return parser.parse_args()


def main():
    args = get_args()
    results = sp.album(args.aid)
    pprint(results)


if __name__ == '__main__':
    main()
