from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    father_school = models.ForeignKey(
        "self", default=None, on_delete=models.CASCADE, blank=True, null=True
    )
    
    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        "self", default=None, on_delete=models.CASCADE, blank=True, null=True
    )
    ai_data_hash = models.CharField(max_length=64, blank=True, null=True)
    school = models.ForeignKey(
        School , on_delete=models.CASCADE, blank=True, null=True
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name if self.name else self.email

    def save(self, *args, **kwargs):  # pragma: no cover
        if self._state.adding is True:
            self.date_joined = now()
        super(CustomUser, self).save(*args, **kwargs)