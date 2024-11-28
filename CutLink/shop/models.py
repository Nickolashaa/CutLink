from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to="profile_pictures", default="photo_default.png")
    text = models.TextField(default="Я так обожаю сладкий раф с сахаром и карамельным сиропом :)")
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        
    def __str__(self):
        return f"Профиль пользователя {self.user}"
    
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.image.path)
            
            
class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_url = models.TextField()
    second_url = models.TextField()
    
    
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        
    def __str__(self):
        return f"Ссылка пользователя {self.user}"