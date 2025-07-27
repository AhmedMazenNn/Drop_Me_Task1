from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepositViewSet, RewardSummaryViewSet

router = DefaultRouter()
router.register(r'deposits', DepositViewSet, basename='deposit')
router.register(r'summaries', RewardSummaryViewSet, basename='summary')

urlpatterns = [
    path('', include(router.urls)),
]
