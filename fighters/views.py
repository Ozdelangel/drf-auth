from rest_framework import generics
from .serializer import FightersSerializer
from .models import Fighters
from .permissions import IsOwnerOrReadOnly

class FightersList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer

class FightersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer
