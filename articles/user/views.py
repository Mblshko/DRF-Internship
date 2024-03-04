from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles.user.models import User, Profile
from articles.user.serializers import (UserRegisterSerializer, ProfileRegisterSerializer,
                                       ProfileDetailSerializer, ProfileUpdateSerializer)


@api_view(["POST"])
def register(request):
    serializer_user = UserRegisterSerializer(data=request.data)
    serializer_profile = ProfileRegisterSerializer(data=request.data)

    if serializer_user.is_valid() and serializer_profile.is_valid():
        user = serializer_user.validated_data
        profile = serializer_profile.validated_data
        u = User.objects.create_user(**user)
        Profile.objects.create(user_id=u, **profile)
        return Response({"message": "Регистрация прошла успешно."}, status=status.HTTP_201_CREATED)
    return Response(serializer_profile.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'nickname'
    slug_field = "nickname"
    slug_url_kwarg = "nickname"


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'nickname'
