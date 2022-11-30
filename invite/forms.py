from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wedding, Guest, Song, Food, Message


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


class RSVPForm(forms.ModelForm):
    RSVP = forms.NullBooleanField(label="RSVP")
    RSVP_comment = forms.JSONField(label="RSVP Comment")

    class Meta:
        model = Guest
        fields = ["RSVP", "RSVP_comment"]


class AddSong(forms.ModelForm):
    song = forms.TextInput()
    artist = forms.TextInput()

    class Meta:
        model = Song
        fields = ["song", "artist"]


class EditProfile(forms.ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField(required=True)
    phone = forms.TextInput()
    hotel = forms.TextInput()

    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "email", "phone", "hotel"]


class EditDiet(forms.ModelForm):
    allergies = forms.TextInput()
    diet = forms.TextInput()

    class Meta:
        model = Food
        fields = ["allergies", "diet"]


class FoodQuestionnaire(forms.ModelForm):
    starter = forms.ChoiceField(
        widget=forms.Select,
        choices=Food.STARTER_CHOICES,
        )
    main = forms.ChoiceField(
        widget=forms.Select,
        choices=Food.MAIN_CHOICES,
        )
    dessert = forms.ChoiceField(
        widget=forms.Select,
        choices=Food.DESSERT_CHOICES,
        )
    allergies = forms.TextInput()
    diet = forms.TextInput()

    class Meta:
        model = Food
        fields = ["starter", "main", "dessert", "allergies", "diet"]  # noqa


class MessageForm(forms.ModelForm):
    title = forms.TextInput()
    description = forms.JSONField

    class Meta:
        model = Message
        fields = ["title", "description"]
