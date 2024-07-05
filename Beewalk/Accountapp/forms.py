from django import forms
from .models import Member

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_img = forms.ImageField(required=False)

    class Meta:
        model = Member
        fields = ['username', 'email', 'password','profile_img']
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)