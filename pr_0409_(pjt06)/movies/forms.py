from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    # 영화제목
    title = forms.CharField(
        label = '영화 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control mb-3 center-block',
                'maxlength': 10,
                'placeholder': '제목을 입력해주세요. : 제목은 10자가 최대입니다.',
                'style':'max-width: 600px'
            }
        )
    )

    # 관객 수 
    audiance = forms.IntegerField(
        label = '관객 수',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control mb-3',
                'placeholder': '관객 수를 입력해주세요.',
                'style':'max-width: 600px'
            }
        )
    )

    # 개봉일
    release_date = forms.DateField(
        label = '개봉일',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control mb-3',
                'placeholder': '개봉일을 입력해주세요. : yyyy-mm-dd',
                'style':'max-width: 600px'
            }
        )
    )
    # 장르
    genre_choices = [('코미디', '코미디'), ('공포', '공포'), ('로맨스', '로맨스')]
    genre = forms.ChoiceField(
        label = '장르 선택',
        choices = genre_choices,
        widget = forms.Select(
            attrs = {
            'class': 'form-select mb-3',
            'style':'max-width: 600px'
            }
        )
    )
    # 스코어
    score = forms.FloatField(
        label = '평점',
        widget = forms.NumberInput(
            attrs = {
                'step': 0.5, 
                'max': 5.0, 
                'min': 0.0,
                'placeholder': '평점을 입력해주세요. : 0 ~ 5점까지 0.5 씩 올라갑니다.',
                'class': 'form-control mb-3',
                'style':'max-width: 600px'

            }
        )
    )
    # 포스터 경로
    poster_url = forms.CharField(
        label = '이미지 주소',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control mb-3',
                'placeholder': '포스터의 이미지 주소를 입력해주세요.',
                'style':'max-width: 600px'
            }
        )
    ) 
    # 줄거리
    description = forms.CharField(
        label = '줄거리',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control mb-3',
                'placeholder': '줄거리를 입력해주세요.',
                'style':'max-width: 600px'
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
