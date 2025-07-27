from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Deposit, RewardSummary
from .serializers import DepositSerializer, RewardSummarySerializer


class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Deposit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        summary, created = RewardSummary.objects.get_or_create(user=self.request.user)
        summary.update_summary()


class RewardSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RewardSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RewardSummary.objects.filter(user=self.request.user)
