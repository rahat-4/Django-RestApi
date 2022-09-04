from pyexpat import model
from django.db import models
from django.conf import settings

# Create your models here.
def status_image_upload(instance,filename):
    return 'uploads/{instance}/{filename}'.format(instance=instance.user,filename=filename)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=status_image_upload, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.content)[:30]
    
    class Meta:
        verbose_name_plural = 'Status List'