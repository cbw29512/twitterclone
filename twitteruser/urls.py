from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:user_id>', views.profileView, name='profile'),
    path('follow_user/<int:id>', views.follow_user, name='follow'),
    path('unfollow_user/<int:id>', views.unfollow_user, name='unfollow'),
]
