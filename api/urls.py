from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', ViewPosts.as_view(), name= 'request'),
    path('posts/<int:pk>/', PostDetails.as_view(), name= 'details'),
    path('posts', FindPosts.as_view(), name='findposts')
]
