class Album:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def get_album_name(self):
        """Return name of album"""
        return self.name

    def get_album_songs(self):
        """Return songs in album"""
        return self.songs

    def __repr__(self):
        return f"{self.name.title()}: {len(self.songs)} songs"
