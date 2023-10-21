from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import UserProfileSerializer

class GetUserProfileView(APIView):
  def get(self, request, format=None):
    user = User.objects.get(id=self.request.user.id)
    print(f'\n[request user] {self.request.user}', f'\n[user] {user}')

    user_profile = UserProfile.objects.get(user=user)
    serializer = UserProfileSerializer(user_profile)

    return Response(serializer.data)

