from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('editar/', views.editar, name='editar'),
    path('crear/', LoginView.as_view(template_name='principal/crear.html'), name="crear"),
    path('login/', LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='principal/logout.html'), name='logout'),
]