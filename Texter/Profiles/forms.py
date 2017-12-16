from django import forms

class Profile_Login(forms.Form):
    Username = forms.CharField(label='Username', max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput())
