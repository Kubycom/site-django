from .models import Articles
from django.forms import ModelForm
from django.forms import TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announce', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Article's title",
            }),
            'announce': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Article's announce",
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "yy-mm-dd h:m",
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Article's text",
            }),
        }
