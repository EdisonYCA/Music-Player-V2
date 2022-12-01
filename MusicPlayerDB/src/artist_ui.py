from artist import Artist
from album import Album
from song import Song


def ui():
    run_program = True

    while run_program:
        # ask the user to enter their artist name
        print("Welcome to Music Player V2\n"
              "Let's begin by adding your profile to our Artist database!")
        artist_name = input("Enter your artist name -> ")

        # ask the artist to enter a song or album
        print(f"\n{artist_name}, would you like to enter a song, or a album to your profile?\n"
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

            # artist.add_album(album_request())
            print("\nOperation successful!\n")
            print(artist)

        else:
            print("Thank you!")
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

if __name__ == "__main__":
    ui()