from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .api import views as api

app_name = 'userauth'

urlpatterns = [
	path('register/', views.register, name = 'register'),
	path('login/', auth_views.LoginView.as_view()),
	path('logout/', auth_views.LogoutView.as_view()),
	path('index/', views.index, name = 'index'),
	path('list/', api.UserListView.as_view(), name = 'user_list'),
	path('create/', api.UserCreateView.as_view(), name = 'user_create'),
	path('change-password/', auth_views.PasswordChangeView.as_view()),
]