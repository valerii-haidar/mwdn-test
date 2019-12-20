import os
from django import forms


class FileForm(forms.Form):
    file = forms.FileField('File')
