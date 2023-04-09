from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """сроковое отображение модели в админке"""
        return self.text[:50]