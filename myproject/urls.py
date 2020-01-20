from django.contrib import admin
from django.urls import path
from iplocation import views # Import the views from your app

urlpatterns = [
    path('', views.home, name='home'), # Add the right URL to point to the view
    path('search/', views.search_ip, name='search'),
    path('admin/', admin.site.urls),
]
