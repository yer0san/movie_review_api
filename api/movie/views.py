import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MovieSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("q")

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        url = f"{settings.TMDB_BASE_URL}/search/movie"
        params = {
            "api_key": settings.TMDB_API_KEY,
            "query": query,
            "language": "en-US",
        }

        response = requests.get(url, params=params)
        print(response)
        if response.status_code != 200:
            return Response(
                {"error": "Failed to fetch data from TMDB"},
                status=status.HTTP_502_BAD_GATEWAY
            )

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

        return Response(results, status=status.HTTP_200_OK)

