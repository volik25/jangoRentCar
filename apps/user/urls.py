from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignUpView

urlpatterns = [
    path('', views.profile, name='profile'),
    path('sign-in/', LoginView.as_view(template_name='user/sign-in.html', ), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('logout/', views.log_out, name='logout'),
]
