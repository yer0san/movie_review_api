from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.models import Movie, Review
from .serializers import ReviewCreateSerializer, ReviewReadSerializer
from api.tmdb import get_movie_by_id


class MovieReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, external_id):
        movie = get_object_or_404(Movie, external_id=external_id)

        reviews = movie.reviews.all()
        serializer = ReviewReadSerializer(reviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, external_id):
        serializer = ReviewCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get or create movie
        movie = Movie.objects.filter(external_id=external_id).first()

        if not movie:
            tmdb_data = get_movie_by_id(external_id)

            if not tmdb_data:
                return Response(
                    {"error": "Movie not found on TMDB"},
                    status=status.HTTP_404_NOT_FOUND
                )

            movie = Movie.objects.create(**tmdb_data)

        # Prevent duplicate reviews
        if Review.objects.filter(user=request.user, movie=movie).exists():
            return Response(
                {"error": "You already reviewed this movie"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save review
        review = serializer.save(
            user=request.user,
            movie=movie
        )

        return Response(
            ReviewReadSerializer(review).data,
            status=status.HTTP_201_CREATED
        )

