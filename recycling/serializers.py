from rest_framework import serializers
from .models import Deposit, RewardSummary


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['reward_points', 'timestamp', 'user']

    def create(self, validated_data):
        # Automatically associate the logged-in user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class RewardSummarySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = RewardSummary
        fields = ['user_id', 'username', 'email', 'total_weight', 'total_points']
        read_only_fields = ['user', 'total_weight', 'total_points']
