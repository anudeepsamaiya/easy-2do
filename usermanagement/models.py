from django.db import models

from django.contrib.auth.models import (
    AbstractUser, BaseUserManager,
    User
)

#
#  class User(AbstractUser):
#      identifier = models.CharField(unique=True, max_length=10)
#
    #  USERNAME_FIELD = 'identifier'
