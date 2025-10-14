from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Блог, который ведёт пользователь."""
    text = models.CharField(max_length=350)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text

class Entry(models.Model):
    """Информация, представленная пользователем в блоге."""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 101:
            return self.text
        else:
            return f"{self.text[:100]}..."
