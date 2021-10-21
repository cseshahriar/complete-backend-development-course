from django.urls import path

from .views import post_list, post_create, post_update

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/update/', post_update, name='post_update'),
]