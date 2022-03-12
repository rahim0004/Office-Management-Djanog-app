from .models import Employee,StuffInfo
from django.contrib.auth.models import User
from django import forms



class EmployeeForm(forms.ModelForm):
    # validate here
    class Meta:
        model = Employee
        fields = '__all__'


class StuffForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class StuffInfoForm(forms.ModelForm):
    class Meta:
        model = StuffInfo
        fields = ('portfolio_site', 'profile_pic')


class StuffLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password']


