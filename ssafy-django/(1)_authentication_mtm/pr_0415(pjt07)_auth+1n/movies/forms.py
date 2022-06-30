from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label= '영화 제목',
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'maxlength' : 10,
                'placeholder' : '영화제목을 입력하세요',
            }
        )
    )
    description = forms.CharField(
        label = '영화 설명',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control mb-3',
                'placeholder': '영화에 대한 설명을 간단하게 남겨주세요.',
                'style':'max-width: 300px'
            }
        )
    )

    class Meta:
        model = Movie
        exclude = 'user',

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label= '댓글',
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'style':'max-width: 300px'
            }
        )
    )
    class Meta:
        model = Comment
        fields = 'content',