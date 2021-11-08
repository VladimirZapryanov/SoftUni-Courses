from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [x for x in songs]
        self.published = False

    def add_song(self, new_song: Song):
        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        for song in self.songs:
            if song.name == new_song.name:
                return "Song is already in the album."

        self.songs.append(new_song)
        return f"Song {new_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for song in self.songs:
            result += "\n"
            result += f"== {song.get_info()}"

        return result + "\n"
