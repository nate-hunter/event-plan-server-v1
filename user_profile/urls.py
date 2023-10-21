from django.urls import path, include

# from rest_framework.routers import DefaultRouter

from .views import GetUserProfileView


# router = DefaultRouter()
# router.register(f'things', ThingViewSet)

urlpatterns = [
    path('', GetUserProfileView.as_view()),
]
