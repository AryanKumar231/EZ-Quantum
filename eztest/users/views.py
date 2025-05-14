from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer,UserLoginSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes,force_str
from django.core.mail import send_mail
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        verification_link = f"http://localhost:8000/api/users/verify-email/{uid}/{token}/"
        send_mail(
            'Verify your email',
            f'Click to verify: {verification_link}',
            'aryankashyap03873@gmail.com',
            [user.email],
        )
        return Response({'message': 'Check your email for verification'}, status=status.HTTP_201_CREATED)


class VerifyEmailView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            return Response({'error': 'Invalid link'}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_verified = True
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })