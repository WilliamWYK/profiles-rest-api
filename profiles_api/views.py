from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Similar to traditional django view',
            'give the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
