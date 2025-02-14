# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Voter(models.Model):

    #__Voter_FIELDS__
    fname = models.TextField(max_length=255, null=True, blank=True)
    lname = models.TextField(max_length=255, null=True, blank=True)
    barangay = models.TextField(max_length=255, null=True, blank=True)
    precinct = models.CharField(max_length=255, null=True, blank=True)

    #__Voter_FIELDS__END

    class Meta:
        verbose_name        = _("Voter")
        verbose_name_plural = _("Voter")


class Benefits(models.Model):

    #__Benefits_FIELDS__
    benefitdesc = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Benefits_FIELDS__END

    class Meta:
        verbose_name        = _("Benefits")
        verbose_name_plural = _("Benefits")



#__MODELS__END
