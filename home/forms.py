from django import forms
from .models import Abstract, Author


class AbstractForm(forms.ModelForm):
    class Meta:
        model = Abstract
        exclude = ["upload_datetime"]

        labels = {
            'title': 'Abstract title',
            "abstract_text": "Abstract text"
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            "abstract_text": forms.Textarea(
                attrs={'placeholder': 'Abstract body should be limited to 300 words...',
                'class': 'form-control'})
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ["abstract"]
        
        labels = {
            'first_name': 'First name',
            "middle_initial": "Middle initial",
            "last_name": "Last name",
            "email": "Email address",
            "affiliation": "Affiliation"
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_initial': forms.TextInput(attrs={'placeholder': '(Not required)',
                'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            "affiliation": forms.TextInput(attrs={'class': 'form-control'})
        }
