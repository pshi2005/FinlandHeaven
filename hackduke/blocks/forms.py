from django import forms

from .models import Userlogin

class PostForm(forms.ModelForm):

    class Meta:
        model = Userlogin
        fields = ('user', 'password',)

    usr = Meta.fields[0]