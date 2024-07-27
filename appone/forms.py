from django import forms
from .models import Prep, Review

class PrepForm(forms.ModelForm):
    class Meta:
        model = Prep
        fields = ["subject"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["subject"]