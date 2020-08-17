from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=10)
    user = models.CharField(max_length=20,unique=True)
    phone = models.CharField(max_length=10)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user']

    objects = CustomUserManager()

    def __str__(self):
        return self.user


class Posts(models.Model):
    job_poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=False)
    job_desc = models.TextField(null=False)
    qualifications = models.CharField(max_length=30)
    experience = models.CharField(max_length=20)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.job_title


class Applications(models.Model):
    applicant = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Posts, on_delete=models.CASCADE, default=None)
    notes = models.TextField()
    resume = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.applicant.email
