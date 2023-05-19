from django import forms
from django.contrib.auth.models import User
from .models import Profile, Budget


class SignUp(forms.ModelForm):
    class Meta:
        model=User
        fields = ["first_name", "last_name", "email","username", "password"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ["address1", "Bank_name", "Branch","state", "bvn", "card_number", "amount", "phone_number"]

class budgetForm(forms.ModelForm):
    class Meta:
        model=Budget
        fields = ["name", "amount", "user","is_income"]




