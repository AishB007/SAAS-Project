from .models import PlanFeature
from django.utils import timezone

def get_plan_features(plan):
    features = PlanFeature.objects.filter(plan=plan)
    return {f.feature.name: f.value for f in features}

def can_user_create_project(user, current_count):
    subscription = user.subscription_set.filter(status='active').first()
    
    if not subscription:
        return False, "No active subscription"

    features = get_plan_features(subscription.plan)
    
    limit = int(features.get("Projects", 0))

    if current_count >= limit:
        return False, "Limit reached"

    return True, "Allowed"

def change_user_plan(user, new_plan):
    subscription = user.subscription_set.filter(status='active').first()

    if not subscription:
        raise Exception("No active subscription")

    subscription.plan_id = new_plan
    subscription.start_date = timezone.now()
    subscription.save()

    return subscription

