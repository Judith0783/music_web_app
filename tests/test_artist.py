from lib.artist import Artist
def test_constructs():
    artist = Artist(1, "Wild Nothing", "Indie")
    assert artist.id == 1
    assert artist.artist_name == "Wild Nothing"
    assert artist.genre == "Indie"
    
    