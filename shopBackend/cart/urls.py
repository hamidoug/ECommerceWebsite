from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartFeedView.as_view(), name='cart'),
    path('cart/<int:pk>', views.CartItemView.as_view(), name='cart-item-detail')
]