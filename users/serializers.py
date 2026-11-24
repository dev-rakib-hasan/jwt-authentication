from rest_framework import serializers
from .models import CustomUser, Blog



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

        

# from rest_framework import serializers
# from .models import CustomUser


# class RegisterSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(
#         write_only=True,
#         min_length=8
#     )

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)


# class LoginSerializer(serializers.Serializer):

#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

      