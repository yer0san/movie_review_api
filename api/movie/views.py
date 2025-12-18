from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from api.tmdb import search_movies

class MovieSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("q")

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        results = search_movies(query)

        if results is None:
            return Response(
                {"error": "Failed to fetch data from TMDB"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        return Response(results, status=status.HTTP_200_OK)


