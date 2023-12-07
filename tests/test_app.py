# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
#   Scenario 1

# POST /albums
#   title: "In Ear Park"
#   release_year: 2008
#   artist_id: 1
#   Expected Response (200 OK)

"""
(No content)
"""

# GET /albums
#  Expected response (200 OK):

#Album(1, The Cold Nose, 2008, 1)
#Album(2, In Ear Park, 2008, 2)
"""
When I call GET /album
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, The Cold Nose, 2008, 1)"
"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '1'   
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, The Cold Nose, 2008, 1)\n" \
        "Album(2, In Ear Park, 2008, 1)"
        
def test_post_albums_with_not_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, The Cold Nose, 2008, 1)"
        


#   Scenario 2

# POST /albums
# Expected Response (400 Bad Request)

"""
You need to submit a title, release_year, and artist_id
"""
# GET /albums
#  Expected response (200 OK):

"""
Album(1, The Cold Nose, 2008, 1)
"""