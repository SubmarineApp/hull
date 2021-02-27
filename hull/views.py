import django_filters
from rest_framework import viewsets, generics

from .serializers import CategorySerializer, SubscriptionSerializer
from .models import Subscription, Category

class SubscriptionFilter(django_filters.FilterSet):
    starts_at = django_filters.DateFilter(field_name="starts_at", lookup_expr="gte")
    ends_at = django_filters.DateFilter(field_name="ends_at", lookup_expr="lte")
    class Meta:
        model = Subscription
        fields = ('id', 'starts_at', 'ends_at', 'category')

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().order_by('starts_at')
    serializer_class = SubscriptionSerializer
    filter_class = SubscriptionFilter

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
