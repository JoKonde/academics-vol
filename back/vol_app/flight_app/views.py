# flight_app/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Compagnie, Vol, MonVol, User, Contact, Payment
from .serializers import CompagnieSerializer, VolSerializer, MonVolSerializer, UserSerializer, ContactSerializer, PaymentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes

# Exemple de vue API
class CompagnieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Compagnie.objects.all()
    serializer_class = CompagnieSerializer
    permission_classes = [permissions.IsAuthenticated]  # Exemple de permission

# Vue API pour obtenir un vol spécifique
class VolRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vol.objects.all()
    serializer_class = VolSerializer
    permission_classes = [permissions.AllowAny]  # Permission ouverte pour cet exemple

# Vue API pour créer un MonVol
class MonVolCreateAPIView(generics.CreateAPIView):
    queryset = MonVol.objects.all()
    serializer_class = MonVolSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vue API pour gérer l'authentification avec JWT
class TokenObtainPairView(TokenObtainPairView):
    pass  # Déjà implémenté par rest_framework_simplejwt

# flight_app/views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except AuthenticationFailed as e:
            return Response(
                {"detail": "Aucun compte actif trouvé avec les identifiants fournis."},
                status=status.HTTP_401_UNAUTHORIZED
            )


# Exemple de vue basée sur fonction
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def home(request):
    return HttpResponse("Welcome to the Flight App API")

