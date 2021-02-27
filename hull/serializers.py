from rest_framework import serializers

from .models import Subscription, Category

class SubscriptionSerializer(serializers.ModelSerializer):
    next_recurrence = serializers.DateField()
    class Meta:
        model = Subscription
        fields = ('id', 'title', 'category', 'starts_at', 'trial_ends_at', 'ends_at', 'recurrence', 'trial_cost', 'cost', 'next_recurrence')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
