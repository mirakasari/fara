from rest_framework import serializers
from atlas.models import Atlas, DISHES,  COUNTRY_CHOICES

class AtlasSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dish = serializers.CharField(required=False, allow_blank=True)
    country = serializers.ChoiceField(choices=COUNTRY_CHOICES, default='friendly')

    def create(self, validated_data):
        return Atlas.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.dishes = validated_data.get("dishes", instance.dishes)
        instance.country = validated_data.get("country", instance.country)
        instance.save()
        return instance 
    
class AtlasSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="atlas-highlight", format="html"
    )

    class Meta:
        model = Atlas 
        fields = [
            "created",
            "dishes",
            "owner"
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    atlas = serializers.HyperlinkedRelatedField(
        many=True, view_name="atlas-detail", read_only=True
    )

    class Meta:
        model = User 
        fields = ["url", "id", "username", "atlas"]