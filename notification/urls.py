from django.urls import path
from notification.views import notification_view


urlpatterns = [
   path('notification/<str:id>', views.notification, name='unfollow'),
]
