from django.urls import path
from . views import (PostListView,
                     PostDetailView, PostCreateView, PostUpdateView,
                     PostDeleteView
                     )
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name="bloghome"),
    path('<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="aboutus"),

]
