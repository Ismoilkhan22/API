from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from views.models import User
from views.serializer import UserSerializer


class LoginView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        if 'email' not in data or 'password' not in data:
            return Response({'error': "password or email is incomplete "})
        user = User.objects.filter(email=data['email'])
        if not user:
            return Response({"error": " user does not exist"})
        if not user.check_password(str(data['password'])):
            return Response({"error": "password is mistake "})
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            "result": token.key
        })


class RegisView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        password = request.data.get('password')
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(str(password))
        user.save()
        return Response({
            "result": "Ro'yhatdan o'tildi "
        })








