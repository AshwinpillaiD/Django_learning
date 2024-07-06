from django.urls import (path,
                         )
from . import views

urlpatterns = [
    path('member',views.home,name='member'),
    path('blog_home',views.blog_home,name='blog_home'),
    path('blog_details',views.blog_details,name='blog_details'),
    path('profile',views.profile,name='profile'),
]