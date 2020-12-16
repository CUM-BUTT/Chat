from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import UserSignInForm, UserLogInForm


def index(request) -> object:
    return render(request, 'main/html/index.html')

# registration
def log_in(request):
    if request.method == 'POST':
        form = UserLogInForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    form = UserLogInForm()
    context = {'form':form}
    return render(request, 'main/html/log_in.html', context)

# authorization
def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')

    form = UserSignInForm()
    return render(request, 'main/html/sign_in.html', {'form': form})

def log_out(request):
    logout(request)
    return render(request, 'main/html/index.html')





