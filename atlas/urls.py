from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from atlas import views 

router = DefaultRouter() 
router.register(r'atlas', views.AtlasViewSet, basename="atlas")
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'restaurants', views.RestaurantViewSet, basename="restaurant")

urlpatterns = [
    path("", include(router.urls)),
    path("countries/", views.CountryList.as_view(), name="country-list"),
    path("cuisines/", views.CuisineList.as_view(), name="cuisine-list"),
    path("dishes/", views.DishList.as_view(), name="dish-list"),
]