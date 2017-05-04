
from django import forms

from pagedown.widgets import PagedownWidget
from django.forms.utils import flatatt
from .models import Post

from __future__ import unicode_literals

import copy
import datetime
import re
from itertools import chain

from django.conf import settings
from django.forms.utils import flatatt, to_current_timezone

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]
