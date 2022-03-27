from rest_framework import generics
from .serializer import FightersSerializer
from .models import Fighters
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class FightersList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer

class FightersDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer
