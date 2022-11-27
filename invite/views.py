from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from wedding_invite import settings


def get_sign_in(request):
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.user.is_authenticated:
        return redirect("/invite/")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {User.first_name, User.last_name}.")  # noqa
                    return redirect("/invite/")
                else:
                    messages.error(request, "Invalid email or password.")
        form = AuthenticationForm()
    context = {
        'login_form': form,
        'wedding': wedding
    }
    return render(request=request, template_name='invite/index.html', context=context)  # noqa


def register_request(request):
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/invite/")
        messages.error(request, "Unsuccessful registration. Invalid information.")  # noqa
    form = forms.NewUserForm()
    context = {
        'register_form': form,
        'wedding': wedding
    }
    return render(request=request, template_name="invite/register.html", context=context)  # noqa


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def password_reset_request(request):
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "invite/password/password_reset_email.txt"  # noqa
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)  # noqa
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    context = {
        'password_reset_form': password_reset_form,
        'wedding': wedding
    }
    return render(request=request, template_name="invite/password/password_reset.html", context=context)  # noqa


@login_required(login_url='/')
def get_invite(request):
    guest = models.Guest.objects.filter(user_id=request.user.id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.method == 'POST':
        form = forms.RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/invite/')
    form = forms.RSVPForm()
    context = {
        'form': form,
        'guest': guest,
        'wedding': wedding,
    }
    return render(request, 'invite/invite.html', context)


@login_required(login_url='/')
def get_info(request):
    guest = models.Guest.objects.filter(user_id=request.user.id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.filter(guest_id=request.user.id).first()
    hotel = models.Hotel.objects.all()
    key = settings.GOOGLE_API_KEY
    context = {
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'hotel': hotel,
        'key': key,
    }
    return render(request, 'invite/info.html', context)


@login_required(login_url='/')
def get_gallery(request):
    wedding = models.Wedding.objects.filter(active=True).first()
    images = models.Image.objects.all()
    context = {
        'wedding': wedding,
        'images': images
    }
    return render(request, 'invite/gallery.html', context)


@login_required(login_url='/')
def get_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest = models.Guest.objects.filter(user_id=user_id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.all()
    song = models.Song.objects.filter(guest=guest)
    context = {
        'user': user,
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'song': song,
    }
    return render(request, 'invite/profile.html', context)


@login_required(login_url='/')
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest = get_object_or_404(models.Guest, user_id=user.id)
    food = models.Food.objects.filter(guest_id=guest.id)
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.method == 'POST':
        profile_form = forms.EditProfile(request.POST, instance=guest)
        if not food:
            if profile_form.is_valid():
                profile_form.save()
                return redirect(get_profile, user_id=request.user.id)
        else:
            diet_form = forms.EditDiet(request.POST, instance=food)
            if profile_form.is_valid() and diet_form.is_valid():
                profile_form.save()
                diet_form.save()
                return redirect(get_profile, user_id=request.user.id)
    profile_form = forms.EditProfile(instance=guest)
    if not food:
        context = {
            'user': user,
            'guest': guest,
            'wedding': wedding,
            'profile_form': profile_form,
        }
    else:
        diet_form = forms.EditDiet(instance=food)
        context = {
            'user': user,
            'guest': guest,
            'wedding': wedding,
            'profile_form': profile_form,
            'diet_form': diet_form
        }
    return render(request, 'invite/edit_profile.html', context)


@login_required(login_url='/')
def get_add_song(request):
    guest = models.Guest.objects.filter(user_id=request.user.id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    form = forms.AddSong()
    if request.method == "POST":
        form = forms.AddSong(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guest_id = guest.id
            obj.save()
            if 'add_another' in request.POST:
                return redirect('/add_song/')
            elif 'exit' in request.POST:
                return redirect(get_profile, user_id=request.user.id)
    context = {
        'guest': guest,
        'wedding': wedding,
        'form': form
    }
    return render(request, 'invite/add_song.html', context)


def delete_song(request, song_id):
    song = get_object_or_404(models.Song, id=song_id)
    song.delete()
    return redirect(get_profile, user_id=request.user.id)


@login_required(login_url='/')
def get_party_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest = models.Guest.objects.filter(user_id=user_id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.all()
    song = models.Song.objects.filter(guest=guest)
    context = {
        'user': user,
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'song': song,
    }
    return render(request, 'invite/profile.html', context)
