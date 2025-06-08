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
    

class Alert(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('classified', 'Classificado'),
    ]

    message = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.message[:50]}... ({self.status})"
