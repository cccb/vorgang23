
"""
Vorgang 23 :: Auth Models
"""

import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser


def _make_api_key():
    """Create an api key"""
    return secrets.token_hex(8)


def _make_api_secret():
    """Create an api secret"""
    return secrets.token_urlsafe(64)


class User(AbstractUser):
    """Vorgang23 User Model"""

    # As users might be scripts, we assign an
    # api key and secret, which can be used to access the service:
    api_key = models.CharField(max_length=16,
                               default=_make_api_key)

    api_secret = models.CharField(max_length=86,
                                  default=_make_api_secret)

