from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute ('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["artist_name"], row["genre"])
            artists.append(item)
        return artists
            
       