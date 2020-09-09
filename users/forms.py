from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=('username','email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class UserDetails(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields = "__all__"
