from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
