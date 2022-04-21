from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Article, Comment, User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user', 'like_users')

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)