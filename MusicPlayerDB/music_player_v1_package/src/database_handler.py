import os

artist_name_test = "Kid Cudi"

parent_dir = "C:\\Desktop\\Python\\MusicPlayerDB\\database\\Artists\\"

path = os.path.join(parent_dir, artist_name_test)
albums_path = os.path.join(path, "Albums")
songs_path = os.path.join(path, "Songs")

os.makedirs(path)
os.makedirs(albums_path)
os.makedirs(songs_path)
