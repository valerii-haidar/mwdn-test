# -*- coding: utf-8 -*-
from crawler.forms import FileForm
from django.views.generic import TemplateView


class UploadFileView(TemplateView):
    template_name = 'templates/upload.html'

    def get_context_data(self, **kwargs):
        context = super(UploadFileView, self).get_context_data(**kwargs)
        context['form'] = FileForm()
        return context
