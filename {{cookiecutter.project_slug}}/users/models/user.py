from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers.user import UserManager


class User(AbstractUser):
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    {%- if cookiecutter.username_type == "email" %}
    email = models.EmailField(_("email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    {%- endif %}

    def __str__(self):
        return f'{self.email} -#{self.id}'
    

