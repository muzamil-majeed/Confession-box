from django import forms
from .models import Confession,Comment



class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ["content_title","content"]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content":forms.Textarea(attrs={
                "rows":3,
                "placeholder":"Write Your Comment"
            })
        }