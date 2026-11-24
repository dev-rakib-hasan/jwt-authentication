from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Blog
from drf_spectacular.utils import (
    extend_schema,
    OpenApiRequest,
    OpenApiResponse
)

from .serializers import(
    RegisterSerializer,
    LoginSerializer,
    BlogSerializer
)
# Create your views here.
@extend_schema(
    tags=['Register'],
    summary="Register a new user.",
    request=RegisterSerializer,
    responses=RegisterSerializer,
)

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
    
@extend_schema(
    tags=['Login'],
    summary="Log in a new user.",
    request=LoginSerializer,
    responses={
        200:LoginSerializer,
        201:OpenApiResponse(description='created'),
        400:OpenApiResponse(description='Bad Request.'),
        401:OpenApiResponse(description='Unauthorized.')
    }
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
#====================
# Blog Api
#====================

@extend_schema(
    tags=['Blog'],
    summary='create Blog',
    description=('Retrieve all blog or New blog'),
    request=BlogSerializer,
    responses={
        200:BlogSerializer(many=True),
        201:OpenApiResponse(description='Added Successfully,.'),
        400:OpenApiResponse(description='Validation Error')
    },
)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def blog_list_create(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    if not request.user.is_authenticated:
        return Response(
            {'message':'Authentication Required'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    serializer = BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=['Blog'],
    summary='Retrieve update or delete blog',
    description='Retrieve Update or delete using ID.',
    request=BlogSerializer,
    responses={
        200:BlogSerializer,
        204:OpenApiResponse(description='Blog Deleted Successfully'),
        400:OpenApiResponse(description='Validation Error'),
        404:OpenApiResponse(description='Blog Not Found')
    },
)

@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
        if request.method == 'PATCH':
            serializer = BlogSerializer(
                blog,
                data=request.data,
                partial=True
                )
        else: 
            serializer = BlogSerializer(
                blog,
                data=request.data
                )
            
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        blog.delete()
        return Response({'message':'Blog Deleted Succesfully.'},status=status.HTTP_204_NO_CONTENT)
    