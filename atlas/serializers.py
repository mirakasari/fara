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