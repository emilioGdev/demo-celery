from django.db import models

class Demo(models.Model):
    LEVEL_CHOICES = [
        ('info', 'Informativo'),
        ('warning', 'Aviso'),
        ('critical', 'Crítico'),
    ]

    message = models.TextField()
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.level}] {self.message[:30]}"