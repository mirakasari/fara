from rest_framework import serializers
from atlas.models import Atlas
from django.contrib.auth.models import User

class AtlasSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
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