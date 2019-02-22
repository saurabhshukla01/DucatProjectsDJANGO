from .models import Profile
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={}),
        required=True, max_length=30
    )
    class Meta:
        model = Profile
        fields = ['username','email','first_name','last_name','password','is_seller','description', 'photo']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        email = user.email
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('please write valid email address')
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')
    #
    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = Profile.objects.get(email=email)
    #     except Profile.DoesNotExist:
    #         # Unable to find a user, this is fine
    #         return email
    #
    #     # A user was found with this as a username, raise an error.
    #     raise forms.ValidationError('This email address is already in use.')

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


