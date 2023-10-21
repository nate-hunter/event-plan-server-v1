from django.urls import path, include

from .views import GetCSRFToken, RegisterView, LoginView, LogoutView, DeleteAccountView, CheckAuthenticatedView, GetUsersView

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('csrf', GetCSRFToken.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),

    path('users', GetUsersView.as_view()),
]
