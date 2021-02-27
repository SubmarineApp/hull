from rest_framework import serializers

from .models import Subscription

class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'title', 'starts_at', 'trial_ends_at', 'ends_at', 'recurrence', 'trial_cost', 'cost')
