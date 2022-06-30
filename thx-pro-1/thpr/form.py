from dataclasses import field
from .models import TextMessage
from django import forms

class TextMessageForm(forms.ModelForm):
    class Meta:
        model = TextMessage
        fields = '__all__'
