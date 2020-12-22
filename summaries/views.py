from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Summary
from .serializers import SummarySerializer

class SummaryList(ListCreateAPIView):
  queryset = Summary.objects.all()
  serializer_class = SummarySerializer

class SummaryDetail(RetrieveUpdateDestroyAPIView):
  queryset = Summary.objects.all()
  serializer_class = SummarySerializer