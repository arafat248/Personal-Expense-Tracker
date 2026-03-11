from djoser.serializers import UserCreateSerializer, UserSerializer

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'email', 'password')

class CustomUserSerializer(UserSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'password')