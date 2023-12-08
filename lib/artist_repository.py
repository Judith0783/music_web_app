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
            
    def create(self, artist):
        self._connection.execute(
            'INSERT INTO artists (artist_name, genre) VALUES(%s, %s)',
            [artist.artist_name, artist.genre])
        return True
    
  