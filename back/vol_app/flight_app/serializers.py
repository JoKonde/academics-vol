# flight_app/serializers.py

from rest_framework import serializers
from .models import Compagnie, Vol, MonVol, User, Contact, Payment

class CompagnieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compagnie
        fields = '__all__'  # Inclut tous les champs du modèle Compagnie

class VolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vol
        fields = '__all__'  # Inclut tous les champs du modèle Vol

class MonVolSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonVol
        fields = '__all__'  # Inclut tous les champs du modèle MonVol

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Inclut tous les champs du modèle User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'  # Inclut tous les champs du modèle Contact

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Inclut tous les champs du modèle Payment
