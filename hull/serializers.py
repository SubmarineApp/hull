from rest_framework import serializers

from .models import Subscription, Category

class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'title', 'category', 'starts_at', 'trial_ends_at', 'ends_at', 'recurrence', 'trial_cost', 'cost')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
