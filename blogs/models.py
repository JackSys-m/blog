from django.db import models

class BlogPost(models.Model):
    """Тема блога, который ведёт пользовтель"""
    text = models.CharField(max_length=350)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text