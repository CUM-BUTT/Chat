from django.shortcuts import render
from .forms import UserLogSignInForm, UserSignInForm, UserLogInForm


def index(request) -> object:
    return render(request, 'main/html/index.html')


# зарегистрироваться
def log_in(request):
    if request.method == 'POST':
        form = UserLogSignInForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            context = {'user': user}
            return render(request, 'main/html/index.html', context)

    form = UserLogInForm()
    return render(request, 'main/html/log_in.html', {'form': form})



def log_out(request):
    context = {'is_user_logged_in': False}
    return render(request, 'main/html/index.html')


# авторизоваться
def sign_in(request):
    if request.method == 'POST':
        form = UserLogSignInForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            context = {'user': user}
            return render(request, 'main/html/index.html', context)

    form = UserSignInForm()
    return render(request, 'main/html/sign_in.html', {'form': form})


