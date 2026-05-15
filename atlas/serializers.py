from rest_framework import serializers
from atlas.models import Atlas, Restaurant
from django.contrib.auth.models import User

class CountrySerializer(serializers.Serializer):
    country = serializers.CharField()

class CuisineSerializer(serializers.Serializer):
    cuisine = serializers.CharField()

class DishSerializer(serializers.Serializer):
    dish = serializers.CharField()

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
            "owner",
            "highlight"
        ]
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
            "owner",
            "highlight"
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    atlas = serializers.HyperlinkedRelatedField(
        many=True, view_name="atlas-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "atlas"]