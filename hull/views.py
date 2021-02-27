from rest_framework import viewsets

from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().order_by('starts_at')
    serializer_class = SubscriptionSerializer
