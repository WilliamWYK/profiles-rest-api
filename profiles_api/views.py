from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

class HelloAPIView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Similar to traditional django view',
            'give the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our post name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request,pk=None):
        """Update(replace) with a new object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partial Update with object fields"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewsets(viewsets.ViewSet):
    """Test View sets"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):

        an_viewset = [
            "User actions (list, create, retrieve, update, partial_update)",
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello Viewsets','an_viewset':an_viewset})
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            message = serializer.validated_data.get('name')
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by ID"""
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """Handle update(replace) an object """
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handle update part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle delete an Object"""
        return Response({'http_method':'DELETE'})