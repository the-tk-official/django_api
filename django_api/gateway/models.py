from django.db import models

from user.models import CustomUser

# Create your models here.

class Jwt(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='login_user')
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email}  |  {self.created_at}  |  {self.updated_at}'
