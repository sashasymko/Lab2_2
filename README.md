# Lab2_2
Spotify API

Name: lab2_2

The aim: to get information from Spotify by user`s choice.

In this module such libraries were used:
- os;
- base64;
- json;
- dotenv (load_dotenv);
- requests (post, get).

There are 6 functions:

1) get_token: this function gets access token to work further with other functions.
2) get_auth_headers: this function gets authorization headers.
3) search_for_artists: this function searches for the right artist.
4) get_most_popular_song_by_artist: this function searches for the most popular song by the artist.
5) get_songs_by_artist: this function searches for the top 10 songs by the artist.
6) user: special function to communicate with user.

If you run the program user will see:

What artist do you need?:

Depending on what the user wants to know, he should choose one of the desired options:

Make a choice:
1. Artist name
2. The most popular song by the artist
3. Artist`s ID
4. List of 10 popular songs
5. Genres
6. The most famous album by the artist
