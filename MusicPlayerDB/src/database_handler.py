import os
from pathlib import Path

PARENT_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = Path(PARENT_DIR) / 'database'
ARTISTS_IN_DATABASE_DIR = Path(DATABASE_DIR) / 'Artists'


def store_artist(artist_name):
    albums_dir = Path(ARTISTS_IN_DATABASE_DIR) / artist_name / 'Albums'
    songs_dir = Path(ARTISTS_IN_DATABASE_DIR) / artist_name / 'Songs'

    # create folders: "songs, albums" in the artists directory
    try:
        os.makedirs(albums_dir)
        os.makedirs(songs_dir)
    except FileExistsError:
        print("I'm sorry, '" + artist_name + "'" + " is already stored in the database.\nTerminating process..")
        exit()


def store_song(artist_name, song_name):
    song_name += ".txt"
    # fetch the artists location in the database and append song_name
    artist_path = Path(ARTISTS_IN_DATABASE_DIR) / artist_name / 'Songs' / song_name
    # store the song in the song folder for that artist
    open(artist_path, 'w')


def store_album(artist_name, album_name, songs):
    # check for song count before storing album
    if len(songs) < 2:
        print("In order to create an album, the album must include at-least 2 songs.")
    else:
        # fetch the artists location in the database
        artist_path = Path(ARTISTS_IN_DATABASE_DIR) / artist_name / 'Albums' / album_name
        # create folder in artists location with album_name
        try:
            os.mkdir(artist_path)
        except FileExistsError:  # restriction: artist cannot have multiple albums with the same name
            print(f"{album_name} already exists in {artist_name}'s profile.")
        # store songs in album
        for song in songs:
            song += ".txt"
            open(artist_path / song, 'w')


def locate_artist(artist_name):
    location = os.path.join(ARTISTS_IN_DATABASE_DIR, artist_name)
    if os.path.isdir(location):
        return location
    return False
