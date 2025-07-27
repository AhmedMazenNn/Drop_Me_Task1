from django.contrib import admin
from .models import Deposit, RewardSummary

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'material_type', 'weight_kg', 'reward_points', 'machine_id', 'timestamp')
    list_display_links = ('id', 'user')
    list_filter = ('material_type', 'timestamp')
    search_fields = ('user__email', 'material_type', 'machine_id')
    readonly_fields = ('reward_points', 'timestamp')
    ordering = ('id',)

@admin.register(RewardSummary)
class RewardSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_weight', 'total_points')
    list_display_links = ('id', 'user')
    search_fields = ('user__email',)
    ordering = ('-total_points',)
