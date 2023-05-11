from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['city', 'mascot']
        widgets = {
            'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
            'mascot': forms.TextInput(attrs={'placeholder': 'Enter mascot'}),
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        }
