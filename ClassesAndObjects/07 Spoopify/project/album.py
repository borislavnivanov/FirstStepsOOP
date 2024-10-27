from project.song import Song


class Album:
    def __init__(self, name: str, *args: Song):
        self.name = name
        self.songs: list[Song] = [el for el in args]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return 'Cannot remove songs. Album is published.'
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f'Removed song {song_name} from album {self.name}.'
        else:
            return 'Song is not in the album.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self) -> str:
        formated_album = [f'Album {self.name}']
        for song in self.songs:
            formated_album.append(song.get_info())
        return '\n== '.join(formated_album) + '\n'
