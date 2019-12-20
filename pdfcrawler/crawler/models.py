# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    name = models.CharField(
        'Document name',
        max_length=255
    )

    def __str__(self):
        return self.name


class Url(models.Model):
    documents = models.ManyToManyField(
        Document,
        verbose_name='Document',
        related_name='urls'
    )
    address = models.URLField('Url', unique=True)

    def __str__(self):
        return self.address

