from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StoreItem
from .serializers import StoreItemSerializer

# Create your views here.

#View To Display Store feed and add items to it
class StoreFeedView(APIView):
    #Display Entire Store Feed
    def get(self, request):
        try:
            storeitems = StoreItem.objects.all()
            serializer = StoreItemSerializer(storeitems, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #Add an Item to the Store Feed
    def post(self, request):
        try:
            serializer = StoreItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Invalid data provided', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#View to display individual store items, edit them, and delete them
class StoreItemView(APIView):
    #Display Individual Store Item
    def get(self, request, pk):
        try:
            storeitem = StoreItem.objects.get(pk=pk)
            serializer = StoreItemSerializer(storeitem)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except StoreItem.DoesNotExist:
            return Response({'error': 'StoreItem not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    #Edit Individual Store Item
    def put(self, request, pk):
        try: 
            storeitem = StoreItem.objects.get(pk=pk)
            serializer = StoreItemSerializer(storeitem, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid data provided', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        
        except StoreItem.DoesNotExist:
            return Response({'error': 'StoreItem not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, pk):
        try:
            storeitem = StoreItem.objects.get(pk=pk)
            storeitem.delete()
            return Response({'message': 'StoreItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
        except StoreItem.DoesNotExist:
            return Response({'error': 'StoreItem not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'detials': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)