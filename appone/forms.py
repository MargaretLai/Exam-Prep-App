from django import forms
from .models import Prep, Review, EmailSubscriber

class PrepForm(forms.ModelForm):
    class Meta:
        model = Prep
        fields = ["subject"]
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["subject"]
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class EmailSignupForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ["email"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

