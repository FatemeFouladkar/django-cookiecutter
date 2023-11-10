from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers.user import UserManager


class User(AbstractUser):
    first_name = models.CharField(
        max_length=200,
        verbose_name=_('First name'),
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name=_('Last name'),
        blank=True,
        null=True
    )
    {%- if cookiecutter.username_type == "email" %}
    email = models.EmailField(_("Email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    {%- endif %}
    objects = UserManager()

    def __str__(self):
        return f'{self.email} -#{self.id}'
    

