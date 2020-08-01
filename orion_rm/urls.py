from django.contrib import admin
from django.urls import path, include

from users.views import login_view, logout_view
from users import urls as user_urls

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('users/', include(user_urls, namespace='users')),
]
