from django.urls import path
from atlas import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("atlas/<int:pk>/", views.AtlasDetail.as_view()),
    path("atlas/", views.AtlasList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)