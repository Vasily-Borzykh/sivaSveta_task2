from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)  # Поле для описания
    
    def __str__(self):
        return self.description or "Image"
