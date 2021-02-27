from django.db import models
from datetime import date

class Subscription(models.Model):
    class RecurrenceType(models.TextChoices):
        WEEKLY = 'weekly'
        MONTHLY = 'monthly'
        YEARLY = 'yearly'

    title = models.CharField(max_length=100)
    starts_at = models.DateField(default=date.today)
    trial_ends_at = models.DateField(null=True)
    ends_at = models.DateField(null=True)
    recurrence = models.CharField(max_length=20, choices=RecurrenceType.choices)
    trial_cost = models.PositiveIntegerField(null=True)
    cost = models.PositiveIntegerField(default=0)
