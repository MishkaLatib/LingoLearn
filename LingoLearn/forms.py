from django.contrib.auth.models import User
from django import forms

#form class to handle user inputs for LingoLearn site registration

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

#indicates fields to be filled in by users
    #does not submit until all fields filled
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']




