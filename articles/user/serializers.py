from rest_framework import serializers

from articles.user.models import User, Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]


class ProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["nickname", "first_name", "last_name"]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "created_at", "last_login"]


class ProfileDetailSerializer(serializers.ModelSerializer):
    user_id = UserDetailSerializer(many=False)

    class Meta:
        model = Profile
        fields = ["nickname", "first_name", "last_name", "user_id"]


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["first_name", "last_name"]


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)
