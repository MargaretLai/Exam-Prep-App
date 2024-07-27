from django import forms
from .models import Prep

class PrepForm(forms.ModelForm):
    class Meta:
        model = Prep
        fields = ["subject"]