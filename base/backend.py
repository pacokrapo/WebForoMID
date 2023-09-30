from django.contrib.auth.backends import BaseBackend
from .models import User

class MyUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):

        try:
            # Obtiene la instancia del usuario
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # Verifica la contraseña
        if user.check_password(password):
            return user
        return None

    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None