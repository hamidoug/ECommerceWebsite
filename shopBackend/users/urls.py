from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.UserView.as_view(), name='user-detail'),
    path('register/', views.RegisterView.as_view(), name='register')
]
