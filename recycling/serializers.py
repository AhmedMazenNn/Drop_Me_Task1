from rest_framework import serializers
from .models import Deposit, RewardSummary


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['reward_points', 'timestamp', 'user']

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight must be greater than zero.")
        if value > 1000:  # optional sanity limit
            raise serializers.ValidationError("Weight seems too high. Please check again.")
        return value

    def validate_material_type(self, value):
        allowed_types = ['plastic', 'metal', 'glass']  # adjust to match your model
        if value.lower() not in allowed_types:
            raise serializers.ValidationError(f"Material type must be one of: {', '.join(allowed_types)}.")
        return value.lower()

    def create(self, validated_data):
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
