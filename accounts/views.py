from django.contrib import auth
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.models import UserProfile

# from .serializers import UserSerializer


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
  def get(self, request, format=None):
    user = self.request.user

    try:
      isAuthenticated = user.is_authenticated

      if isAuthenticated:
        return Response({'isAuthenticated': 'succes'})
      else:
        return Response({'isAuthenticated': 'error'})

    except:
      return Response({'error': 'Something went wrong checking authentication status'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
  permission_classes = (permissions.AllowAny, )

  def get(self, request, format=None):
    return Response({'success': 'CSRF cookie set'})


@method_decorator(csrf_protect, name='dispatch')
class RegisterView(APIView):
  permission_classes = (permissions.AllowAny, )

  def post(self, request, format=None):
    data = self.request.data

    username = data['username']
    password = data['password']
    re_password = data['re_password']

    try:
      if password != re_password:
        return Response({'error': 'Passwords do not match'})
      if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'})
      if len(password) < 6:
        return Response({'error': 'Password must be at least 6 characters'})

      user = User.objects.create_user(username=username, password=password)
      user = User.objects.get(id=user.id)
      user_profile = UserProfile.objects.create(
        user=user,
        first_name='',
        last_name='',
        phone_number_1='',
        address_city='',
      )
      return Response({'success': 'User created'})

    except:
      return Response ({'error': 'Something went wrong registering account'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
  permission_classes = (permissions.AllowAny, )

  def post(self, request, format=None):
    data = self.request.data

    username = data['username']
    password = data['password']

    try:
      user = auth.authenticate(username=username, password=password)

      if user is None:
        return Response({'error': 'Error logging in'})

      auth.login(request, user)
      return Response({'success': 'User authenticated'})

    except:
      return Response({'error': 'Something went wrong logging in'})




class LogoutView(APIView):
  def post(self, request, format=None):
    try:
      auth.logout(request)
      return Response({'sucess': 'Logged out'})

    except:
      return Response({'error': 'Something went wrong logging out'})