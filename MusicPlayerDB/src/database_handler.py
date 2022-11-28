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
        print("'" + artist_name + "'" + " is already stored in the database.")


def store_song(artist_name, song_name):
    song_name += ".txt"
    # fetch the artists location in the database and append song_name
    artist_path = Path(ARTISTS_IN_DATABASE_DIR) / artist_name / 'Songs' / song_name
    # store the song in the song folder for that artist
    song = open(artist_path, 'w')


def store_album(artist_name, album_name, songs):
    pass
    # fetch the artists location in the database
    # create folder in artists location with album_name
    # create files in album_name with song names


