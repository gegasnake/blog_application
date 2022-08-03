from .views import DataListView, BlogDetailView
from django.urls import path
urlpatterns = [
    path('', DataListView.as_view(), name="home"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]