"""
lab2_task2
Python_Spotify_API
"""
import os
import base64
import json
from dotenv import load_dotenv
from requests import post, get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    """
    get access token 
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_headers(token):
    """
    getting authorization headers 
    """
    return {"Authorization": "Bearer " + token}

def search_for_artists(token, artist_name):
    """
    the fuctions searches for the right artists
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_headers(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artists with this name exists...")
        return
    return json_result[0]

def get_most_popular_song_by_artist(token, artist_name):
    """
    getting the most popular song by artist
    """
    artist = search_for_artists(token, artist_name)
    if not artist:
        return
    url = f"https://api.spotify.com/v1/artists/{artist['id']}/top-tracks?country=US"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    if len(json_result) == 0:
        print("No tracks found for the artist...")
        return
    most_popular_song = json_result[0]["name"]
    most_pop_album = json_result[0]["album"]["name"]
    return most_popular_song, most_pop_album, json_result[0]["id"]

def get_songs_by_artist(token, artist_id):
    """
    getting famous songs by artist_id
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def user():
    """
    user navigation
    """
    token = get_token()
    artist_name = input("What artist do you need?: ")
    artist = search_for_artists(token, artist_name)
    if not artist:
        return
    print("Make a choice:")
    print("1. Artist name")
    print("2. The most popular song by the artist")
    print("3. Artist`s ID")
    print("4. List of 10 popular songs")
    print("5. Genres")
    print("6. The most famous album by the artist")
    option = None
    while option not in ['1', '2', '3', '4', '5', '6']:
        option = input("Enter an option number: ")
        if option not in ['1', '2', '3', '4', '5', '6']:
            print("Please enter a number between 1 and 6.")
    if option == '1':
        result = search_for_artists(token, artist_name)
        print(result["name"])
    if option == '2':
        song, _, _= get_most_popular_song_by_artist(token, artist_name)
        print(song)
    if option == '3':
        _,  _, song_id = get_most_popular_song_by_artist(token, artist_name)
        print(song_id)
    if option == '4':
        result = search_for_artists(token, artist_name)
        artist_id = result["id"]
        songs = get_songs_by_artist(token, artist_id)
        for index, song in enumerate(songs):
            print(f"{index + 1}. {song['name']}")
    if option == '5':
        result = search_for_artists(token, artist_name)
        genres = result["genres"]
        if len(genres) > 0:
            print("Genres:")
            for i, genre in enumerate(genres):
                print(f"{i+1}. {genre}")
        else:
            print("No genres found for the artist...")
    if option == '6':
        _, album, _ = get_most_popular_song_by_artist(token, artist_name)
        print(album)
user()
