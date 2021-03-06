from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.core.signing import BadSignature
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from .utils import signer

from .forms import AccountRegistrationForm


class AccountRegistrationView(CreateView):
    model = get_user_model()
    template_name = 'account/registration.html'
    success_url = reverse_lazy('accounts:registration_done')
    form_class = AccountRegistrationForm


class AccountRegistrationDoneView(TemplateView):
    template_name = 'account/registration_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'account/bad_signature.html')

    user = get_object_or_404(get_user_model(), username=username)
    if user.is_activated:
        template = 'account/user_is_activated.html'
    else:
        template = 'account/activation_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()

    return render(request, template)
