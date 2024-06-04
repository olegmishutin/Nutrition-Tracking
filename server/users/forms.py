from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']

    def save(self, commit=True):
        return get_user_model().objects.create_user(**self.cleaned_data)


class LoginForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['password']
