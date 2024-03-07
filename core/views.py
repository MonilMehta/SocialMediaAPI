from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout,authenticate
from rest_framework.permissions import IsAuthenticated
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .models import Profile,Post,Like
from .serializers import UserRegistrationSerializer, UserLoginSerializer,ProfileSerializer,PostSerializer,LikeSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message':'User created successfully','username': user.get_username()}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user is not None:
                login(request, user)
                token = AuthToken.objects.create(user)[1]
                return Response({'username': user.get_username(), 'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        serializer = ProfileSerializer(instance=user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProfileSerializer(instance=user_profile)
    return Response(serializer.data)
    
@api_view(['GET'])
def signout(request):
    logout(request)
    AuthToken.objects.filter(user=request.user).delete()
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class UserLoginAPIView(KnoxLoginView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createpost(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data, context={'request': request})  # Pass the request context
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getpost(request):
    # Retrieve all posts authored by the current user
    posts = Post.objects.filter(author=request.user)
    # Serialize the posts
    serializer = PostSerializer(posts, many=True)
    # Return the serialized posts as a response
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request):
    if request.method == 'POST':
        post_id = request.data.get('post_id')  
        try:
            post = Post.objects.get(pk=post_id)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if created:
                return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request):
    if request.method == 'POST':
        post_id = request.data.get('post_id')
        if not post_id:
            return Response({'error': 'Post ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            post = get_object_or_404(Post, pk=post_id)
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)