from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Post

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user_bio', 'user_img', 'user_dob']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['author']  

    def create(self, validated_data):
        # Get the authenticated user from the request
        author = self.context['request'].user
        validated_data['author'] = author
        post = Post.objects.create(**validated_data)
        return post