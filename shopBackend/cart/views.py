from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer
from store.models import StoreItem

# Create your views here.

#View To Display Cart feed and add items to it
class CartFeedView(APIView):
    #Function to get whole cart
    def get(self, request):
        try:
            cartitems = CartItem.objects.filter(user=request.user)
            serializer = CartItemSerializer(cartitems, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #Function to add item to cart 
    def post(self, request):
        try: 
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Invalid data provided', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#View To Display and Delete single cart items
class CartItemView(APIView):

    #Function to get one cart item
    def get(self, request, pk):
        try: 
            cartitem = CartItem.objects.get(pk=pk, user=request.user)
            serializer = CartItemSerializer(cartitem)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CartItem.DoesNotExist:
            return Response({'error': 'CartItem not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #Function to delete a cart item
    def delete(self, request, pk):
        try:
            cartitem = CartItem.objects.get(pk=pk, user=request.user)
            cartitem.delete()
            return Response({'message': 'StoreItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except CartItem.DoesNotExist:
            return Response({'error': 'CartItem not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


