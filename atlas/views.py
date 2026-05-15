from atlas.models import Atlas, Restaurant
from atlas.serializers import AtlasSerializer, UserSerializer, RestaurantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import action

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to create entries.
    Read permissions are allowed to any request.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        return request.user and request.user.is_staff

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "atlas": reverse("atlas-list", request=request, format=format),
            "restaurants": reverse("restaurant-list", request=request, format=format),
        }
    )

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AtlasViewSet(viewsets.ModelViewSet):
    queryset = Atlas.objects.all()
    serializer_class = AtlasSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        cuisine = self.request.query_params.get('cuisine')
        dish = self.request.query_params.get('dish')

        if country:
            queryset = queryset.filter(country__iexact=country)
        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)
        if dish:
            queryset = queryset.filter(dish__icontains=dish)

        return queryset

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        atlas = self.get_object()
        return Response(atlas.highlighted)

    @action(detail=True, methods=["post", "delete"], permission_classes=[permissions.IsAuthenticated], url_path="like")
    def like(self, request, *args, **kwargs):
        atlas = self.get_object()
        if request.method == 'POST':
            atlas.likes.add(request.user)
        else:
            atlas.likes.remove(request.user)
        return Response({
            'liked': atlas.likes.filter(pk=request.user.pk).exists(),
            'likes_count': atlas.likes.count()
        })

    @action(detail=True, methods=["get"], url_path="recommended-restaurant")
    def recommended_restaurant(self, request, *args, **kwargs):
        atlas = self.get_object()
        restaurant = atlas.restaurant
        if not restaurant:
            return Response({"detail": "No restaurant recommendation available."}, status=404)
        serializer = RestaurantSerializer(restaurant, context={"request": request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

