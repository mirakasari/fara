from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles 
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight 

DISHES = ['Spaghetti', 'Butter Chicken', 'Mapo Tofu']
COUNTRY_CHOICES = ((0, 'Italy'), (1, 'India'), (2, 'China'))

class Atlas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dishes = models.BooleanField(
        choices = COUNTRY_CHOICES, default='python', max_length=100
    )
    owner = models.ForeignKey(
        "auth.User", related_name="atlas", on_delete=models.CASCADE)

    highlighted = models.TextField() 
    
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

class Meta:
    ordering = ['created']

