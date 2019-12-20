# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from crawler.models import Document, Url
from django.contrib import admin


class UrlTabularInline(admin.TabularInline):
    model = Document.urls.through


class DocumentAdmin(admin.ModelAdmin):
    inlines = [UrlTabularInline]


class UrlAdmin(admin.ModelAdmin):
    list_display = ('address', )


admin.site.register(Document, DocumentAdmin)
admin.site.register(Url, UrlAdmin)
