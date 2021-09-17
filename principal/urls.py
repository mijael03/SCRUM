from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView,PostDetailView,AddPost,UpdatePostView,DeletePostView,AddCommentView,CategoryListView,CategoryView,AddCategoryView

urlpatterns = [
    path('',HomeView.as_view(), name = "home"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('post/<int:pk>',PostDetailView.as_view(), name="post-detail"),
    path('add_post/',AddPost.as_view(), name="add-post"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(), name="update-post"),
    path('post/<int:pk>/remove',DeletePostView.as_view(),name="delete-post"),
    path('logout/', LogoutView.as_view(template_name='principal/logout.html'), name='logout'),
    path('post/<int:pk>/comment',AddCommentView.as_view(),name="add_comment"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
]