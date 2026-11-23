from rest_framework import serializers
from .models import CustomUser


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

      