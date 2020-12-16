from django.forms import ModelForm, TextInput
from .models import User

class UserLogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', ]
        widgets = {'name': TextInput(attrs='name'),
                   'password': TextInput(attrs='password'),}