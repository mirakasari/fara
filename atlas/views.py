from atlas.models import Atlas
from atlas.serializers import AtlasSerializer, UserSerializer
from rest_framework import generics
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
        }
    )

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AtlasViewSet(viewsets.ModelViewSet):
    queryset = Atlas.objects.all()
    serializer_class = AtlasSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        atlas = self.get_object()
        return Response(atlas.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)