from artist import Artist
from album import Album
from song import Song


def ui():
    run_program = True

    while run_program:
        # ask the user to enter their artist name
        print("Let's get your profile set up on our Artist database!")
        artist_name = input("Enter your artist name -> ")

        # ask the artist to enter a song or album
        print(f"\n{artist_name}, would you like to enter a song, or a album to your profile?\n"
              "1. Song\n"
              "2. Album\n"
              "3. None")
        request = input("-> ")

        artist = Artist(artist_name)
        if request == "1":
            song_request(artist)
            print("\nGreat! Here is an overview of your new profile:")
            print(artist)

        elif request.lower() == "2":
            album_request(artist)
            print(artist)

        else:
            print(f"Okay {artist_name}, you're now stored in our database. Thank you!")
            print(artist)

        run_program = False


def album_request(artist):
    albums = []
    while True:
        print("Enter the name of the album")
        album_name = input("-> ")
        print(f"\n{album_name} will at-least two songs.")
        songs = song_request(artist)

        artist.add_album(album_name, songs)
        albums.append(album_name)
        print("Would you like to add another album?\n"
              "1. Yes\n"
              "2. No")
        add_album = input("-> ")
        if add_album == "2":
            break
    print(f"Okay {artist.get_name()}, ", end="")
    print(*albums, sep=", ", end=" ")
    print("are now on your profile!")


def song_request(artist):
    songs = []
    while True:
        print("Enter the name of the song")
        song_name = input("-> ")
        song = song_name + ".txt"

        artist.add_song(song)
        songs.append(song)

        print("Would you like to add another song?\n"
              "1. Yes\n"
              "2. No")
        add_song = input("-> ")

        if add_song == "2":
            break
    return songs


if __name__ == "__main__":
    ui()
