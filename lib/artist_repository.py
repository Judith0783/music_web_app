class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute ('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = Artist(row["artist_name"], row["genre"], row["artist_id"])
            artists.append(item)
        return artists
            
       