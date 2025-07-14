from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("rooms-list")
    
    return render(request, "auth_system/register.html", context={"form":form})

def login_page(request):

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect("rooms-list")
    
    return render(request, "auth_system/login.html", context={"form":form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect("login_page")