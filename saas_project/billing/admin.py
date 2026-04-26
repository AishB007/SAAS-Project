from django.contrib import admin
from .models import Plan, Feature, PlanFeature, Subscription, Payment
# Register your models here.

admin.site.register(Plan)
admin.site.register(Feature)
admin.site.register(PlanFeature)
admin.site.register(Subscription)
admin.site.register(Payment)