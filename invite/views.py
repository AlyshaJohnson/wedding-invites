from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
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

# guest list emails
to = models.Guest.objects.filter(status=1).values('first_name', 'last_name', 'email')  # noqa


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
    return render(request=request, template_name='index.html', context=context)  # noqa


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
    return render(request=request, template_name="register.html", context=context)  # noqa


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
                    email_template_name = "password/password_reset_email.txt"  # noqa
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
    return render(request=request, template_name="password/password_reset.html", context=context)  # noqa


@login_required(login_url='/')
def get_invite(request):
    user = get_object_or_404(User, id=request.user.id)
    guest = get_object_or_404(models.Guest, user_id=user.id)
    wedding = models.Wedding.objects.filter(active=True).first()
    if request.method == 'POST':
        form = forms.RSVPForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('/invite/')
    form = forms.RSVPForm(instance=guest)
    context = {
        'user': user,
        'form': form,
        'guest': guest,
        'wedding': wedding,
    }
    return render(request, 'invite.html', context)


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
    return render(request, 'info.html', context)


@login_required(login_url='/')
def get_gallery(request):
    wedding = models.Wedding.objects.filter(active=True).first()
    images = models.Image.objects.all()
    context = {
        'wedding': wedding,
        'images': images
    }
    return render(request, 'gallery.html', context)


@login_required(login_url='/')
def get_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest = models.Guest.objects.filter(user_id=user_id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.filter(guest_id=guest.id)
    song = models.Song.objects.filter(guest=guest)
    guest_active = models.Guest.objects.filter(status=1)
    guest_draft = models.Guest.objects.filter(status=0)
    rsvp = models.Guest.objects.exclude(RSVP=None)
    context = {
        'user': user,
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'song': song,
        'guest_active': guest_active,
        'guest_draft': guest_draft,
        'rsvp': rsvp
    }
    return render(request, 'profile.html', context)


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
    return render(request, 'edit_profile.html', context)


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
    return render(request, 'add_song.html', context)


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
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def add_food(request):
    user = get_object_or_404(User, id=user_id)
    guest = models.Guest.objects.filter(user_id=request.user.id).first()
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.filter(guest_id=guest.id).first()
    form = forms.FoodQuestionnaire()
    if request.method == 'POST':
        form = forms.FoodQuestionnaire(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guest_id = guest
            obj.save()
            return redirect(get_profile, user_id=request.user.id)
    context = {
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'form': form,
    }
    return render(request, 'add_food.html', context)


@login_required(login_url='/')
def edit_food(request, user_id):
    user = get_object_or_404(User, id=user_id)
    guest = get_object_or_404(models.Guest, user_id=user.id)
    wedding = models.Wedding.objects.filter(active=True).first()
    food = models.Food.objects.filter(guest_id=guest.id).first()
    form = forms.FoodQuestionnaire(instance=food)
    if request.method == 'POST':
        form = forms.FoodQuestionnaire(request.POST, instance=food)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.guest_id = guest
            obj.save()
            return redirect(get_profile, user_id=request.user.id)
    context = {
        'user': user,
        'guest': guest,
        'wedding': wedding,
        'food': food,
        'form': form,
    }
    return render(request, 'edit_food.html', context)


@login_required(login_url='/')
def send_message(request):
    if request.user.is_staff is True:
        guest = models.Guest.objects.filter(user_id=request.user.id).first()
        wedding = models.Wedding.objects.filter(active=True).first()
        form = forms.MessageForm()
        if request.method == 'POST':
            form = forms.MessageForm(request.POST)
            if form.is_valid():
                if 'send' in request.POST:
                    obj = form.save(commit=False)
                    obj.guest_id = guest
                    obj.status = 1
                    obj.save()
                    subject = obj.title
                    message = obj.description
                    from_admin = guest.email
                    send_mail(subject, message, from_admin, to, fail_silently=True)  # noqa
                elif 'save' in request.POST:
                    obj = form.save(commit=False)
                    obj.guest_id = guest
                    obj.status = 0
                    obj.save()
            return redirect("/invite/")
        context = {
            'guest': guest,
            'wedding': wedding,
            'form': form,
        }
        return render(request, 'send_message.html', context)
    else:
        return redirect('/invite/')


def send_invite(request):
    user = get_object_or_404(User, id=user_id)
    guest = get_object_or_404(models.Guest, user_id=user.id)
    wedding = models.Wedding.objects.filter(active=True).first()
    subject = "You're invited to {{ wedding.couple.first.first_name }} & {{ wedding.couple.last.first_name }}'s Wedding"  # noqa
    email_template_name = "Invite.txt"
    c = {
        'to': to,
        'wedding': wedding,
        'email': user.email,
        'domain': 'wdg-invite.herokuapp.com',
        'site_name': 'Website',
        'user': user,
        'protocol': 'http',
    }
    message = render_to_string(email_template_name, c)
    from_admin = guest.email
    send_mail(subject, message, from_admin, to.email, fail_silently=True)  # noqa
    return redirect(get_profile, user_id=request.user.id)
