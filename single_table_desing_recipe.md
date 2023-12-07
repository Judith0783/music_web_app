# Single Table Design Recipe

Test-dirve a route 'POST/artists' to create a new artist:

# Request:
POST /artists

# with body paramater:
name=Beyonce
genre=Pop

# Expected response (200 OK)
(No content)


# Request:
GET /artists

# with body paramater:
name=Beyonce
genre=Pop

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

Your test should assert that the new artist is present in the list of artists returned by GET /artists.



#       1. Extract nouns from the user stories or specification

# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

Nouns:

name
genre


#       2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

|Record                 |Properties
|-----------------------|-------------------------
|artist	                |name, genre


Name of the table (always plural): artists

Column names: name, genre

#       3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
name: text
genre: text



#       4. Write the SQL
-- EXAMPLE
-- file: artists_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);
#       5. Create the table

psql -h 127.0.0.1 database_name < albums_table.sql