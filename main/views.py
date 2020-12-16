from django.shortcuts import render
#from .forms import UserLogInForm
#from .models import User


def index(request) -> object:
    return render(request, 'main/html/index.html')


# зарегистрироваться
def log_in(request):
    if request.method == 'POST':
        form = None#UserLogInForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            context = {'user': user}
            return render(request, 'main/html/log_in.html', context)

    return render(request, 'main/html/log_in.html')


def log_out(request):
    context = {'is_user_logged_in': False}
    return render(request, 'main/html/index.html')


# авторизоваться
def sign_in(request):
    return render(request, 'main/html/sign_in.html')


