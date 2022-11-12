from django.shortcuts import render


def get_sign_in(request):
    return render(request, 'invite/index.html')


def get_invite(request):
    return render(request, 'invite/invite.html')
