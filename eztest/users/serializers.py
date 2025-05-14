from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['email', 'name', 'password', 'password2', 'role']
        extra_kwargs={
        'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        role= attrs.get('role')
        
        if role not in ['operation', 'client']:
            raise serializers.ValidationError("Role must be operation/client")
        
        
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        email= attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        
        
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email= data.get('email')
        
        if not data.get('email'):
            raise serializers.ValidationError("Email is required")
        
        if not data.get('password'):
            raise serializers.ValidationError("Password is required")
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email doesn't exist")
        
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Wrong credentials")
        
        if user and user.is_verified:
            return user
        raise serializers.ValidationError("Verified you mail.")