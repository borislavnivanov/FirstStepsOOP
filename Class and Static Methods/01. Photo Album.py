from math import ceil


class PhotoAlbum:
    PAGE_MAX_COUNT = 4
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for p in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        album_pages = ceil(photos_count / cls.PAGE_MAX_COUNT)
        return cls(album_pages)

    def add_photo(self, label: str) -> str:
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_MAX_COUNT:
                page.append(label)
                return f'{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}'
        return f'No more free slots'

    def display(self) -> str:
        result = f'{"-" * 11}\n'
        for page in range(self.pages):
            result += ' '.join(['[]' for x in self.photos[page] if x]) + '\n'
            result += f'{"-" * 11}\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
