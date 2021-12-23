from django.urls import path

from .views import (
    post_list, post_detail, post_create, post_update, post_delete,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('<int:pk>/detail/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/update/', post_update, name='post_update'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    
    # class base views
    path('cbv/list/', PostListView.as_view(), name='cbv_post_list'),
    path('cbv/<int:pk>/detail/', PostDetailView.as_view(), name='cvb_post_detail'),
    path('cbv/create/', PostCreateView.as_view(), name='cvb_post_create'),
    path('cbv/<int:pk>/update/', PostUpdateView.as_view(), name='cvb_post_update'),
    path('cbv/<int:pk>/delete/', PostDeleteView.as_view(), name='cvb_post_delete'),
]