from django.urls import path
from .views import apiOverview, postList, postDetail, postCreate, postUpdate, postDelete


urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('post-list/', postList, name="post-list"),
    path('post-detail/<int:pk>/', postDetail, name="post-detail"),
    path('post-create/', postCreate, name="post-create"),
    path('post-update/<int:pk>/', postUpdate, name="post-update"),
    path('post-delete/<int:pk>/', postDelete, name="post-delete"),
]