from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5)
    email = forms.EmailField(label='E-Mail')
    password1 = forms.CharField(label='Password', max_length=100, min_length=5)
    password2 = forms.CharField(label='Confirm Password', max_length=100, min_length=5)

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Emails is already registred.')
        return email

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError("Password2 doesn't match Password1")
    #     return p1

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError("Passwords do not match")
