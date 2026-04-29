from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles 

DISHES = ['Spaghetti', 'Butter Chicken', 'Mapo Tofu']
COUNTRY_CHOICES = ((0, 'Italy'), (1, 'India'), (2, 'China'))

class Atlas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dishes = models.BooleanField(
        choices = COUNTRY_CHOICES, default='python', max_length=100
    )

class Meta:
    ordering = ['created']

