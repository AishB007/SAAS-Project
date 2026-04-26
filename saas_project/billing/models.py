from django.db import models
from django.conf import settings



User = settings.AUTH_USER_MODEL     
# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    interval = models.CharField(max_length=20, choices=[
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ])

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PlanFeature(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('plan', 'feature')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)

    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('past_due', 'Past Due')
    ])

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.plan}"
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)