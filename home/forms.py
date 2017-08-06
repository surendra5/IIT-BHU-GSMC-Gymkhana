from django import forms
from django.forms import ModelForm

from home.models import GymkhanaFormModel


class GymkhanaForm(forms.ModelForm):

    class Meta:
        model = GymkhanaFormModel
        fields = ['name', 'roll_no', 'year', 'email', 'events', 'message']

#not required
#class UserForm(forms.ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput)

  #  class Meta:
   #    model = User
   #     fields = ['username', 'email', 'password']


