from .artist import Artist
from .album import Album
from .song import Song


def ui():
    run_program = True

    while run_program:
        # ask the user to enter an artist name
        print("Welcome to Music Player V1\n"
              "Let's begin by adding an artist!")
        artist_name = input("Enter the artist name -> ")

        # ask the user to enter a song or album for the artist
        print(f"\nWould you like to enter a song, or a album for {artist_name}?\n"
              "1. Song\n"
              "2. Album\n"
              "3. None")
        request = input("-> ")

        artist = Artist(artist_name)
        if request == "1":
            song = song_request()
            artist.add_song(song)

            print("Would you like to add another song?\n"
                  "1. Yes\n"
                  "2. No")

            add_song = input("-> ")

            while add_song == "1":
                song = song_request()
                artist.add_song(song)
                print("Would you like to add another song?\n"
                      "1. Yes\n"
                      "2. No")
                add_song = input("-> ")

            print("Operation successful!\n")
            print(artist)

        elif request.lower() == "2":
            print(f"\nLets add an album to {artist_name}'s profile.")

            artist.add_album(album_request())
            print("\nOperation successful!\n")
            print(artist)

        else:
            print("\nOperation successful!\n")
            print(artist)

        run_program = False


def album_request():
    print("Enter the name of the album")
    album_name = input("-> ")

    enter_song = True
    songs = []

    print(f"\n{album_name.title()} will need some songs.")
    while enter_song:
        song = song_request()
        songs.append(song)
        print("Would you like to add another song\n"
              "1. Yes\n"
              "2. No")
        add_song = input("-> ")

        if add_song == "1":
            continue
        elif add_song == "2":
            enter_song = False

    album = Album(album_name, songs)
    return album


def song_request():
    print("Enter the name of the song")
    song_name = input("-> ")

    print(f"Enter the length of {song_name} (in the format: minutes.seconds)")
    song_length = input("-> ")

    user_song = Song(song_name, song_length)
    return user_song
