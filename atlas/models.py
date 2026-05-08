from django.db import models
from django.contrib.auth.models import User

COUNTRY_CHOICES = (
    ('Italy', 'Italy'),
    ('India', 'India'),
    ('China', 'China'),
    ('France', 'France'),
    ('Japan', 'Japan'),
    ('Mexico', 'Mexico'),
    ('Thailand', 'Thailand'),
    ('Greece', 'Greece'),
    ('Spain', 'Spain'),
    ('Turkey', 'Turkey'),
)

class Atlas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    cuisine = models.CharField(max_length=100)
    dish = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, related_name="atlas", on_delete=models.CASCADE
    )
    highlighted = models.TextField(blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.dish} - {self.country} ({self.cuisine})"

