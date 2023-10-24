from django.urls import path, include

from rest_framework.routers import DefaultRouter

from events.views import EventsViewSet


router = DefaultRouter()
router.register(f'events', EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
