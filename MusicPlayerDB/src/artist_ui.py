from artist import Artist
import database_handler as db


def ui():
    run_program = True
    new_user = main()

    while run_program:
        # ask the user to enter their artist name
        artist_name = input("Enter your artist name -> ")

        if not db.locate_artist(artist_name) and new_user == "2":
            print(f"I'm sorry, we weren't able to locate '{artist_name}' in our database.\n")
            exit()
        else:
            artist = artist_name

        if new_user == "1":
            artist = Artist(artist_name).get_name()

        # ask the artist to enter a song or album
        print(f"\n{artist_name}, would you like to enter a song, or a album to your profile?\n"
              "1. Song\n"
              "2. Album\n"
              "3. None")
        request = input("-> ")

        if request == "1":
            song_request(artist)
            print("\nGreat! Here is an overview of your profile: ")
            print(artist)

        elif request.lower() == "2":
            album_request(artist)
            print(f"Success")
            print("Here is an overview of your profile: \n")
            print(artist)

        else:
            print("Success")
            print("Here is an overview of your profile: \n")
            print(artist)

        run_program = False


def main():
    print("Would you like to add a song/album to an existing profile, or create a new profile?"
          "\n1. Create new profile"
          "\n2. Existing profile")
    new = input("-> ")

    if new == "1":
        print("Let's get your profile set up on our Artist database!")

    return new


def album_request(artist):
    albums = []
    while True:
        print("Enter the name of the album")
        album_name = input("-> ")
        print(f"\n{album_name} will at-least two songs.")
        songs = song_request(artist)

        db.store_album(artist, album_name, songs)
        albums.append(album_name)
        print("Would you like to add another album?\n"
              "1. Yes\n"
              "2. No")
        add_album = input("-> ")
        if add_album == "2":
            break
    print("Successfully added album.\n")


def song_request(artist):
    songs = []
    while True:
        print("Enter the name of the song")
        song_name = input("-> ")

        db.store_song(artist, song_name)
        songs.append(song_name)

        print("Would you like to add another song?\n"
              "1. Yes\n"
              "2. No")
        add_song = input("-> ")

        if add_song == "2":
            break
    return songs


if __name__ == "__main__":
    ui()
