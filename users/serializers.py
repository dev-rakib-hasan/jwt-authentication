from rest_framework import serializers
from .models import(
    CustomUser,
    Blog,
    Like,
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
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 
            'slug',
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
            'creaated_at'
        ]
        read_only_fields=[
            'id',
            'username',
            'created_at'
        ]

      