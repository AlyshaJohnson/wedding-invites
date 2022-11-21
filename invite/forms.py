from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wedding, Guest


class NewUserForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class RSVP_form(forms.ModelForm):
    RSVP = forms.NullBooleanField(label="RSVP")
    RSVP_comment = forms.JSONField(
        label="RSVP Comment",
        initial="Send a message to {{ wedding.couple.first.first_name }} & {{ wedding.couple.first.first_name }}."  # noqa
        )

    class Meta:
        model = Guest
        fields = ["RSVP", "RSVP_comment"]
