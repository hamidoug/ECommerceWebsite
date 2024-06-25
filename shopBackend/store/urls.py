from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.StoreFeedView.as_view(), name='store'),
    path('store/<int:pk>', views.StoreItemView.as_view(), name='store-item-detail')
]