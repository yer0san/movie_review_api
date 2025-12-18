from rest_framework import serializers
from api.models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["comment"]


class ReviewReadSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Review
        fields = ["id", "user", "comment", "created_at"]
