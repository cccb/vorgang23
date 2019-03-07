

"""
The repository manages tasks and categories
"""

from django.db import models
from django.utils import timezone

from vorgang.bureau import models as bureau_models


class Category(models.Model):
    """Categories organize tasks"""
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)


class Task(models.Model):
    """A model for tasks"""
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)

    priority = models.CharField(max_length=40)

    # Credits override, if no credits are provided,
    # the minutes logged into the task are counted as credit.
    credits = models.IntegerField(null=True)

    # Timeing and Window
    duration = models.DurationField(null=True)
    not_before = models.DateTimeField(default=timezone.now)
    not_after = models.DateTimeField(null=True, blank=True)

    # Relations
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT)

    agents = models.ManyToManyField(bureau_models.Agent)

    # Meta
    created_at = models.DateTimeField(default=timezone.now)

