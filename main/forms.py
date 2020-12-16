from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput
from .models import User

class UserLogSignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', ]
        widgets = {'name': TextInput(attrs={'placeholder': 'name'}),
                   'password': TextInput(attrs={'placeholder': 'password'}), }


# зарегистрироваться
class UserLogInForm( UserCreationForm):
    model = User
    fields = ['name', 'password', ]
    widgets = {'name': TextInput(attrs={'placeholder': 'name'}),
               'password': TextInput(attrs={'placeholder': 'password'}), }



# авторизоваться
class UserSignInForm( AuthenticationForm):
    model = User
    fields = ['name', 'password', ]
    widgets = {'name': TextInput(attrs={'placeholder': 'name'}),
               'password': TextInput(attrs={'placeholder': 'password'}), }