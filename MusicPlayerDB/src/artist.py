import database_handler as db
import os


class Artist:
    def __init__(self, name):
        self.name = name
        db.store_artist(self.name)  # store artist in database
        # dictionary containing of the information on the artist
        self.information = {"database_location": db.locate_artist(self.name),
                            "Albums": self.get_albums(),
                            "Songs": self.get_songs()}

    def get_albums(self):
        """Returns an artists albums with song count"""
        # Locate artist in database
        albums_location = os.path.join(db.locate_artist(self.name), 'Albums')

        albums_list = []
        # Iterate through album names and print them
        song_count = 0
        for albums in os.listdir(albums_location):
            album_name = albums
            albums_list.append(album_name)
        return albums_list

    def get_songs(self):
        """Returns an artists songs"""
        # Locate artist in database
        songs_location = os.path.join(db.locate_artist(self.name), 'Songs')

        song_names = []
        # Iterate through albums
        for songs in os.listdir(songs_location):
            format_song_name = songs.split(".txt")
            song_names.append(format_song_name[0])

        return song_names

    def get_name(self):
        """Returns artists name"""
        return self.name.title()

    def __repr__(self):  # fix string representation of Artists
        """Represent artist object as a string"""
        songs = self.get_songs()
        albums = self.get_albums()
        return f"Artist: {self.name.title()}\n" \
               f"Albums: {', '.join(albums)}\n" \
               f"Songs: {', '.join(songs)}"

