from django.urls import path
from .views import list_plans, user_subscription, change_plan

urlpatterns = [
    path('plans/', list_plans),
    path('subscription/', user_subscription),
    path('change-plan/', change_plan),
]

