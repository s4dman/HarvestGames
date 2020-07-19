from django.urls import path
from .views import registration_view, login_view, logout_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
