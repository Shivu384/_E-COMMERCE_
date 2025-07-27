import django.urls
from django.urls import path, include
from authcart import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
