from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Summary
from .serializers import SummarySerializer

class SummaryList(ListCreateAPIView):
  queryset = Summary.objects.all()
  serializer_class = SummarySerializer

class SummaryDetail(RetrieveUpdateAPIView):
  queryset = Summary.objects.all()
  serializer_class = SummarySerializer