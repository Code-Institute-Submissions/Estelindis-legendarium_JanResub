from .models import Category, Story, Comment
from django import forms


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category_name', 'category_pic',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
