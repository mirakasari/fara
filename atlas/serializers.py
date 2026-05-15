from rest_framework import serializers
from atlas.models import Atlas, Restaurant
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Restaurant
        fields = [
            "url",
            "id",
            "created",
            "name",
            "country",
            "city",
            "cuisine_type",
            "rating",
            "description",
            "owner"
        ]

class AtlasSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    restaurant_name = serializers.ReadOnlyField(source="restaurant.name")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="atlas-highlight", format="html"
    )
    # Prefer the normalized country if available, otherwise fall back to the string field
    country = serializers.SerializerMethodField()
    # Prefer the normalized country if available, otherwise fall back to the string field
    country = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Atlas
        fields = [
            "url",
            "id",
            "created",
            "country",
            "cuisine",
            "dish",
            "restaurant",
            "restaurant_name",
            "likes_count",
            "is_liked",
            "owner",
            "highlight"
        ]

    def get_country(self, obj):
        if getattr(obj, 'country_obj', None):
            return obj.country_obj.name
        return obj.country

    def get_country(self, obj):
        if getattr(obj, 'country_obj', None):
            return obj.country_obj.name
        return obj.country

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if not request or not request.user or not request.user.is_authenticated:
            return False
        return obj.likes.filter(pk=request.user.pk).exists()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    atlas = serializers.HyperlinkedRelatedField(
        many=True, view_name="atlas-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "atlas"]