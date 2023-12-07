from lib.album_repository import AlbumRepository
from lib.album import Album
"""
 When i call #all   
 I get all the albumsin the albums table
"""
def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "The Cold Nose", 2008, 1)
    ]
    
"""
When I call #create
I create an album in the db
And I can see it back in #all    
"""

def test_create(db_connection):
     db_connection.seed("seeds/record_store.sql")
     repository = AlbumRepository(db_connection)
     album = Album(None, "Test Title", 1000, 2)
     repository.create(album)
     assert repository.all() == [
         Album(1, "The Cold Nose", 2008, 1),
         Album(2, "Test Title", 1000, 2)
     ]