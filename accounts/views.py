from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, SigninSerializer


# Create your views here.
@api_view(['POST'])
def Signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Signup Successful.', 'user':serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view({'POST'})
def Signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save():
        return Response({'message': 'Signin Successful.', 'user':serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.erros)