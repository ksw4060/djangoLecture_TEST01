from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.first_view, name='first_test'),
    path('', include('user.urls')),
    path('', include('tweet.urls')),
]
