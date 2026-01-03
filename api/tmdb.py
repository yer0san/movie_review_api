import requests
from django.conf import settings

BASE_URL = settings.TMDB_BASE_URL
API_KEY = settings.TMDB_API_KEY


def search_movies(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query,
        "language": "en-US",
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    results = []
    for movie in data.get("results", []):
        results.append({
            "external_id": movie["id"],
            "title": movie["title"],
            "overview": movie["overview"],
            "release_date": movie["release_date"],
            "poster_url": (
                f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                if movie.get("poster_path")
                else None
            ),
            "rating": movie["vote_average"],
        })

    return results


def get_movie_by_id(external_id):
    url = f"{BASE_URL}/movie/{external_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(response)
        return None

    data = response.json()

    return {
        "external_id": data["id"],
        "title": data["title"],
        "overview": data["overview"],
        "release_date": data["release_date"] or None,
        "poster_url": (
            f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
            if data.get("poster_path")
            else None
        ),
        "rating": data["vote_average"],
    }
