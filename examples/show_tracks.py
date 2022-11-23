# Show artist and track name for list of track IDs
import argparse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from utils import spotify

client_credentials_manager = SpotifyClientCredentials(client_id=spotify.CLIENT_ID,
                                                      client_secret=spotify.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_args():
    parser = argparse.ArgumentParser(description='Get multiple tracks')
    parser.add_argument('-t', '--tids', action='append',
                        required=True, help='Track ids')
    return parser.parse_args()


def main():
    args = get_args()
    results = sp.tracks(args.tids)
    for track in results['tracks']:
        print(track['name'] + ' - ' + track['artists'][0]['name'])


if __name__ == '__main__':
    main()
