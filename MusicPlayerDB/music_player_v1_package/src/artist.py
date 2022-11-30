class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = None
        self.songs = None

    def get_albums(self):
        """Returns a list of artists albums"""
        return self.albums

    def print_albums(self):
        """Returns a string of artists albums"""
        album_names = "None"
        if self.albums is not None:
            album_names = ""
            for album in range(len(self.albums)):
                album_names += str(self.albums[album])
                album_names += "\t\t"
            return album_names
        return album_names

    def print_songs(self):
        """returns a string of artists songs"""
        song_names = "None"
        if self.songs is not None:
            song_names = ""
            for song in range(len(self.songs)):
                song_names += str(self.songs[song])
                song_names += "\t"
            return song_names
        return song_names

    def get_name(self):
        """Returns artists name"""
        return self.name.title()

    def get_songs(self):
        """Returns an artists songs"""
        return self.songs

    def add_album(self, album):
        """add album to artists current album list"""
        for song in range(len(album.songs)):  # all songs in album should also be added into the artists song list
            self.add_song(album.songs[song])

        if self.get_albums() is None:
            self.albums = []
            self.albums.append(album)
        else:
            self.albums.append(album)

    def add_song(self, song):
        """add song to artists current song list"""
        if self.get_songs() is None:
            self.songs = []
            self.songs.append(song)
        else:
            self.songs.append(song)

    def __repr__(self):
        """Represent artist object as a string"""
        return f"Artist: {self.name.title()}\n" \
               f"Albums: {str(self.print_albums())}\n" \
               f"Songs: {str(self.print_songs())}"
