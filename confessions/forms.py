from django import forms
from .models import Confession



class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ["content_title","content"]