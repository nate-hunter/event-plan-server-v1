from django.urls import path, include

from rest_framework.routers import DefaultRouter

from something.views import ThingViewSet


router = DefaultRouter()
router.register(f'things', ThingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
