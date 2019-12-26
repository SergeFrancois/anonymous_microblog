from django.contrib import admin
from django.urls import path
from anonymous_microblog_app import views

urlpatterns = [
    path('', views.show_posts_or_create_new, name='home'),
    path('admin/', admin.site.urls),
]
