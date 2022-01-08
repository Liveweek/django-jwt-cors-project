from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
        Сериализатор катомного токена, для которого было
        добавлено поле имени пользователя (username)
    """
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['username'] = user.username
        return token