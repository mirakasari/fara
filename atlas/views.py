from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from atlas.models import Atlas
from atlas.serializers import AtlasSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from atlas.models import Atlas 
from atlas.serializers import AtlasSerializer 
from django.http import Http404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import mixins 
from rest_framework import generics 

class AtlasList(generics.ListCreateAPIView):
    queryset = Atlas.objects.all() 
    serializer_class = AtlasSerializer 

class AtlasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atlas.objects.all() 
    serializer_class = AtlasSerializer 