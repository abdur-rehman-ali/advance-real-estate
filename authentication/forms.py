from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(
    widget=forms.TextInput(attrs={
      'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
      'placeholder': 'Username'
    })
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={
      'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
      'placeholder': 'Password'
    })
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={
      'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
      'placeholder': 'Repeat Password'
    })
  )

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
  username = forms.CharField(
    widget=forms.TextInput(attrs={
      'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
      'placeholder': 'Username'
    })
  )
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={
      'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
      'placeholder': 'Password'
    })
  )
