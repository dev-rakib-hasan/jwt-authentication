from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from serializers import(
    RegisterSerializer,
    LoginSerializer,
)
# Create your views here.

@api_view(['POST'])
def register(request):
    
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        return Response({
            'message':'Registration Successfull.',
            'user':serializer.data}, 
            status=status.HTTP_201_CREATED
        )
        
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def login(request):
    
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = authenticate(
            request,
            username=email,
            password=password
        )
        if user is not None:
         refresh = RefreshToken.for_user(user)

         return Response({
                'message': 'Login successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
        })
         
        return Response({'eror':'Invalid Email Or Password'},status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)