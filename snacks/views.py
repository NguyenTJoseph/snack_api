from rest_framework import generics
from .models import Snack
from .serializer import SnackSerializer
from .permissions import IsAuthorOrReadOnly

class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

