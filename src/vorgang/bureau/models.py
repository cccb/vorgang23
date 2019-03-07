
"""
The bureau manages agents.
"""

from django.db import models

from vorgang.auth import models as auth_models


class Role(models.Model):
    """When a task is joined by a user, a role is assigned"""
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)


class Agent(models.Model):
    """A task is executed by an agent. Might be a script."""
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

