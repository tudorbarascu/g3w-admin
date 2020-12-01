# coding=utf-8
""""
Usermanage signals receiver
.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2020-11-19'
__copyright__ = 'Copyright 2015 - 2020, Gis3w'


from django.conf import settings
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_updated, social_account_added, pre_social_login
from allauth.account.signals import user_signed_up
from allauth.socialaccount.providers.base import AuthProcess
from allauth.account.utils import perform_login, app_settings
from usersmanage.models import Userbackend, Group as AuthGroup, User
from usersmanage.configs import G3W_VIEWER1, G3W_EDITOR1, G3W_EDITOR2, USER_BACKEND_DEFAULT, USER_BACKEND_SOCIAL


def set_user_backend(user, backend=USER_BACKEND_DEFAULT):
    """Set user backend"""

    if hasattr(user, 'userbackend'):
        user.userbackend.backend = backend
        user.userbackend.save()
    else:
        Userbackend(user=user, backend=backend).save()


@receiver(social_account_updated)
@receiver(user_signed_up)
def add_backend2user(sender, **kwargs):

    # user_signed_up signal
    if 'user' in kwargs:
        user = kwargs['user']
        backend = USER_BACKEND_DEFAULT
    else:
        user = kwargs['request'].user
        backend = USER_BACKEND_DEFAULT

    if not user.is_anonymous:
        AuthGroup.objects.get(name=G3W_EDITOR1).user_set.add(user)
        set_user_backend(user, backend)

from allauth.exceptions import ImmediateHttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

@receiver(pre_social_login)
def check_user(sender, request, sociallogin, **kwargs):

    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users and not sociallogin.is_existing:
         perform_login(request, users[0], email_verification=app_settings.EMAIL_VERIFICATION)
         sociallogin.state["process"] = AuthProcess.CONNECT
    else:
        url = reverse("login")
        ret = HttpResponseRedirect(url)
        raise ImmediateHttpResponse(ret)

