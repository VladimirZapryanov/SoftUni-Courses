<<<<<<< HEAD
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f"{self.lyrics}"


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
=======
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f"{self.lyrics}"


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
