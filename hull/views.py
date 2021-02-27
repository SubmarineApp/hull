import django_filters
import django_property_filter
import datetime
from rest_framework import viewsets

from .serializers import CategorySerializer, SubscriptionSerializer
from .models import Subscription, Category

class SubscriptionFilter(django_property_filter.PropertyFilterSet):
    starts_at = django_filters.DateFilter(field_name="starts_at", lookup_expr="gte")
    ends_at = django_filters.DateFilter(field_name="ends_at", lookup_expr="lte")
    next_recurrence = django_property_filter.PropertyDateFilter(field_name='next_recurrence', lookup_expr='gte')
    recurs_before = django_property_filter.PropertyDateFilter(field_name='next_recurrence', lookup_expr='lte')

    class Meta:
        model = Subscription
        fields = ('id', 'starts_at', 'ends_at', 'category', 'next_recurrence', 'recurs_before')

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().order_by('starts_at')
    serializer_class = SubscriptionSerializer
    filter_class = SubscriptionFilter

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
