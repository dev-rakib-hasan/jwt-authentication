from rest_framework import serializers
from .models import(
    CustomUser,
    Blog,
    Like,
    Comment
)



class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

class LoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
 
 
 
class BlogSerializer(serializers.ModelSerializer):
    
    like_count = serializers.IntegerField(
        source = 'likes.count',
        read_only=True
    )
    comment_count = serializers.IntegerField(
        source ='comments.count',
        read_only = True
    )
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'user',
            'like_count',
            'comment_count',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 
            'slug',
            'user',
            'like_count',
            'comment_count',
            'created_at',
            'updated_at',
        ]

        

class LikeSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(
        source = 'user.username',
        read_only = True   
    )
    class Meta:
        model = Like
        fields = [
            'id',
            'username',
            'blog',
            'created_at'
        ]
        read_only_fields=[
            'id',
            'username',
            'created_at'
        ]

class CommentSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(
        source = 'user.username',
        read_only = True
    )
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'username',
            'blog',
            'content',
            'created_at',
            'updated_at'   
        ]
        read_only_fields=[
            'id',
            'username',
            'created_at'
        ]