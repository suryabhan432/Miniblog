from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm, Textarea


class SignUpForm(UserCreationForm):
	password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		# password1 = forms.CharField(label='password',widget=PasswordInput())
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
		'username':forms.TextInput(attrs={'class':'form-control',}),
		'first_name':forms.TextInput(attrs={'class':'form-control'}),
		'last_name':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'})
		}

class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class Postform(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'desc')
       