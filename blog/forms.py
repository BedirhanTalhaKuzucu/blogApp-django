from django import forms
from .models import Post, Category, Comment

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','content', 'image', 'status')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)