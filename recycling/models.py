from django.db import models
from django.conf import settings

class MaterialType(models.TextChoices):
    PLASTIC = "plastic", "Plastic"
    METAL = "metal", "Metal"
    GLASS = "glass", "Glass"

REWARD_RATES = {
    MaterialType.PLASTIC: 1,
    MaterialType.METAL: 3,
    MaterialType.GLASS: 2,
}

class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='deposits')
    material_type = models.CharField(max_length=10, choices=MaterialType.choices)
    weight_kg = models.FloatField()
    machine_id = models.CharField(max_length=100)
    reward_points = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.reward_points = int(self.weight_kg * REWARD_RATES[self.material_type])
        super().save(*args, **kwargs)

class RewardSummary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='summary')
    total_weight = models.FloatField(default=0)
    total_points = models.PositiveIntegerField(default=0)

    def update_summary(self):
        deposits = self.user.deposits.all()
        self.total_weight = sum(d.weight_kg for d in deposits)
        self.total_points = sum(d.reward_points for d in deposits)
        self.save()
