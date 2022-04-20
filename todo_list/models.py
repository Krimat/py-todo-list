from django.db import models
from django.db.models import UniqueConstraint


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    deadline = models.DateTimeField(
        null=True,
        default=None,
    )

    done = models.BooleanField(
        default=False,
    )

    tags = models.ManyToManyField(
        Tag,
    )

    class Meta:
        ordering = ['done', 'created_at']
