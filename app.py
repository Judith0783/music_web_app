import os
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return "You need to submit a title, release_year, and artist_id", 400
    
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '', 200
  
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(
        f"{album}" for album in repository.all()     
    )

@app.route('/artist', methods=['POST'])
def post_artists():
    if 'artist_name' not in request.form or 'genre' not in request.form:  #not in request.form or 'artist_id' not in request.form:
        return "You need to submit a artist_name and genre", 400
    
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['artist_name'],
        request.form['genre'])
    print(artist)

    repository.create(artist)
    return '', 200


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

#GET ARTISTS
@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return ", ".join(
        f"{artist.artist_name}" for artist in repository.all()     
    )

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

