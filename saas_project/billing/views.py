from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer
from .services import change_user_plan
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def list_plans(request):
    # Logic to list all plans
    print("request:",request)
    plans = Plan.objects.all()
    serializer = PlanSerializer(plans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_subscription(request):
    
    user = request.user
    if not user.is_authenticated:
        return Response({"message": "Not authenticated"}, status=401)
    
    subscription = Subscription.objects.filter(user=user).first()

    if not subscription:
        return Response({"message": "No subscription"})

    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data)



@api_view(['POST'])
def change_plan(request):
    user = request.user
    print(request.data)
    plan_id = request.data.get("plan_id")

    plan = get_object_or_404(Plan, id=plan_id)

    subscription = change_user_plan(user, plan)

    return Response({"message": "Plan updated"})
