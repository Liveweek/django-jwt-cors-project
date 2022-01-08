from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import MyTokenObtainPairSerializer


@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello, world!'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer