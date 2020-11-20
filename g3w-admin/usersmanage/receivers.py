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
from allauth.socialaccount.providers.base import AuthProcess
from allauth.account.utils import perform_login, app_settings
from usersmanage.models import Userbackend, Group as AuthGroup, User
from usersmanage.configs import G3W_VIEWER1, G3W_EDITOR1, G3W_EDITOR2


@receiver(social_account_updated)
def add_backend2user(sender, **kwargs):

    AuthGroup.objects.get(name=G3W_EDITOR1).user_set.add(kwargs['request'].user)


@receiver(pre_social_login)
def test(sender, request, sociallogin, **kwargs):

    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users:
        perform_login(request, users[0], email_verification=app_settings.EMAIL_VERIFICATION)
        sociallogin.state["process"] = AuthProcess.CONNECT

