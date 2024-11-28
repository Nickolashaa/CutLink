from django.shortcuts import render, redirect
from .forms import RegistrationForm, AddUrl
from django.contrib import messages
from .forms import UpdateLoginForm, UpdateTextForm, UpdateImageForm
from django.contrib.auth.decorators import login_required
from .models import Url

# Create your views here.
def home(request):
    return render(request, 'shop/home.html', {
        "title": "CUTLINK"
    })
    
    
def about(request):
    return render(request, 'shop/about.html', {
        "title": "CUTLINK"
    })
    
    
def reg(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Добро пожаловать, {username}")
            form.save()
            return redirect('home')
        return render(request, 'shop/reg.html', {
            "title": "Регистрация",
            "form": form
        })
    else:
        form = RegistrationForm()
        return render(request, 'shop/reg.html', {
            "title": "Регистрация",
            "form": form
        })
        

@login_required
def profile(request):
    if request.method == "POST":
        loginform = UpdateLoginForm(request.POST, instance=request.user)
        textform = UpdateTextForm(request.POST, instance=request.user.profile)
        imageform = UpdateImageForm(request.POST, request.FILES, instance=request.user.profile)
        print(textform.is_valid())
        print(imageform.is_valid())
        print(loginform.is_valid())
        if textform.is_valid() and loginform.is_valid() or imageform.is_valid():
            if textform.is_valid() and loginform.is_valid():
                loginform.save()
                textform.save()
                messages.success(request, f"Профиль обновлен!")
                return redirect("profile")
            else:
                imageform.save()
            messages.success(request, f"Профиль обновлен!")
            return redirect("profile")
    loginform = UpdateLoginForm(instance=request.user)
    textform = UpdateTextForm(instance=request.user.profile)
    imageform = UpdateImageForm(instance=request.user.profile)
    data = {
        "title": "Личный кабинет",
        "loginform": loginform,
        "textform": textform,
        "imageform": imageform,
    }
    return render(request, "shop/profile.html", data)


def urls(request):
    if request.method == "POST":
        form = AddUrl(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.second_url = "link/" + instance.second_url
            instance.save()
            return redirect("urls")
    
    form = AddUrl()
    data = {
        "title": "Мои ссылки",
        "form": form,
        "request": request,
    }
    return render(request, "shop/urls.html", data)