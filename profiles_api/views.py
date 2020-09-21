from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    #"""test api view"""
    def get(self, request, format=None):
    #"""returns a list of APIView features"""
        an_apiview = [
            'uses http methods as function (get,post patch,,put,delete)',
            'is similar to a traditional django view',
            'is mapped manualy to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
