from django import forms
from django.forms import fields,widgets
from .models import Comment,Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        # widgets = {
        #     "article": forms.HiddenInput(),
        #     "writer": forms.HiddenInput(),
        # }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','body')