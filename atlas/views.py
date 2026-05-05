from atlas.models import Atlas
from atlas.serializers import AtlasSerializer
from atlas.serializers import UserSerializer
from rest_framework import generics 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework import renderers 
from rest_framework import viewsets 
from atlas.models import User
from rest_framework import permissions 
from rest_framework import renderers 
from rest_framework.decorators import action 
from rest_framework.response import Response 

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        atlas = self.get_object() 
        return Response(atlas.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)