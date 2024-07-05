# flight_app/urls.py

from django.urls import path
from .views import (
    VolListCreateAPIView, VolRetrieveUpdateDestroyAPIView,
    MonVolListCreateAPIView, MonVolRetrieveUpdateDestroyAPIView,
    CustomTokenObtainPairView,
    # Autres vues importées
)

urlpatterns = [
    # URLs pour Vol
    path('api/vols/', VolListCreateAPIView.as_view(), name='vol-list-create'),
    path('api/vols/<int:pk>/', VolRetrieveUpdateDestroyAPIView.as_view(), name='vol-detail'),

    # URLs pour MonVol
    path('api/monvols/', MonVolListCreateAPIView.as_view(), name='monvol-list-create'),
    path('api/monvols/<int:pk>/', MonVolRetrieveUpdateDestroyAPIView.as_view(), name='monvol-detail'),

    # URLs pour Compagnie, User, Contact, Payment, etc...

    # URL pour l'authentification JWT
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Vous pouvez ajouter d'autres URLs pour le rafraîchissement du token, la révocation, etc...
]

