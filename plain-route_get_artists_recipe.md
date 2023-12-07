{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

#       1. Design the Route Signature

Include the HTTP method, the path, and any query or body parameters.
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)


#       2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

#   Scenario 1

# GET / artists
#   name: ""
#   genre: 
#   Expected Response (200 OK) - Pixies, ABBA, Taylor Swift, Nina Simone


#   Scenario 2

# POST / artists
# Expected Response (400 Bad Request)

"""
You need to submit a name, genre
"""

# Scenario 3 
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie
# Expected response (200 OK)
(No content)

# GET/ artists
# Expected response - (200 OK) 
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


#       3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /artist
  Expected response (200 OK):
  "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'

"""
POST /artist
  Parameters:
    name=Wild nothing
    genre=Indie
  Expected response (200 OK):
  "You need to enter a name and a genre"
"""
def test_post_artist(web_client):
    response = web_client.post('/artist', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
