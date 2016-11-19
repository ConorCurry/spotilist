import sys
import spotipy
import spotipy.util as util
from pprint import pprint

def main():
    scopes = 'playlist-modify-public playlist-modify-private'
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("First argument must be username.")
        sys.exit()

    token = util.prompt_for_user_token(username,scopes)

    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print("Couldn't get token.")
        sys.exit()
    display_playlists(sp)

def display_playlists(sp):
    playlistDataRaw = sp.user_playlists(sp.me()['id'])['items']
    for num,playlist in enumerate(playlistDataRaw):
        print("({:2}) - Playlist: {:15}\tTracks{:15}".format(num, playlist['name'],playlist['tracks']['total']))
    while True:
        selection = input("Which playlist number would you like to modify? ")
        try:
            selection = int(selection)
            assert(selection < len(playlistDataRaw))
            playlistId = playlistDataRaw[selection]['id']
            break
        except:
            print("That's not a valid track identifier.")
    show_playlist(sp, playlistId)

#TODO: Fix this. Getting a HTTP Error 400. Not sure of the problem.
def show_playlist(sp, playlistId, showRange=[0,15]):
    res = sp.user_playlist_tracks(sp.me(), \
                                  playlistId, \
                                  fields='tracks', \
                                  limit=showRange[1]-showRange[0], \
                                  offset=showRange[0])
    pprint(res)
    

def chronosort_playlist():
    pass

main()
