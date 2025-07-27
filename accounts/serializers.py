from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()
    phone = serializers.CharField()

    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'email', 'phone', 'password']

    def validate_username(self, value):
        if UserAccount.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        return value

    def validate_email(self, value):
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate_phone(self, value):
        if not re.fullmatch(r'^01[0-2,5]{1}[0-9]{8}$', value):  # Egyptian mobile number pattern
            raise serializers.ValidationError("Phone number must be a valid Egyptian number.")
        if UserAccount.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number is already in use.")
        return value

    def create(self, validated_data):
        user = UserAccount.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            password=validated_data['password']
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        data['username'] = self.user.username
        return data
