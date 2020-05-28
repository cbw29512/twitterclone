from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:user_id>', views.profileView, name='profile'),
]
