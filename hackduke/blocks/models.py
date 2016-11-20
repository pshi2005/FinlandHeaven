from __future__ import unicode_literals

from django.db import models

class Userlogin(models.Model) :
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
