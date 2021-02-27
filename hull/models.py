from django.db import models
import datetime
import dateutil
from dateutil.relativedelta import *

DEFAULT_CATEGORY_ID = 1

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return (d + datetime.timedelta(days_ahead)).date()

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subscription(models.Model):
    def __str__(self):
        return f'{self.title} - {self.recurrence}'

    class RecurrenceType(models.TextChoices):
        WEEKLY = 'weekly'
        MONTHLY = 'monthly'
        YEARLY = 'yearly'

    title = models.CharField(max_length=100)
    starts_at = models.DateField(default=datetime.date.today)
    trial_ends_at = models.DateField(null=True)
    ends_at = models.DateField(null=True)
    recurrence = models.CharField(max_length=20, choices=RecurrenceType.choices)
    trial_cost = models.PositiveIntegerField(null=True)
    cost = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        default=DEFAULT_CATEGORY_ID
    )

    @property
    def next_recurrence(self):
        if self.trial_ends_at and self.trial_ends_at < datetime.date.today():
            return self.trial_ends_at
        if self.recurrence == 'weekly':
            return next_weekday(datetime.datetime.now(), self.starts_at.weekday())
        if self.recurrence == 'monthly':
            delta = relativedelta(datetime.date.today(), self.starts_at)
            months_since = delta.years * 12 + delta.months
            return self.starts_at + relativedelta(months=months_since + 1)
        if self.recurrence == 'yearly':
            delta =  relativedelta(datetime.date.today(), self.starts_at)
            years_since = delta.years
            return self.starts_at + relativedelta(years=years_since + 1)
