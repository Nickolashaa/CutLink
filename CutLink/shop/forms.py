from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Url


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(label="",
                               max_length=1024,
                               required=True,
                               widget=forms.widgets.TextInput(attrs={
                                   "display": "block",
                                   "class": "username-block css-input",
                                   "placeholder": "Введите ваш Логин",
                                   "helptext": "",
                               }))

    password1 = forms.CharField(label="",
                                max_length=1024,
                                required=True,
                                widget=forms.widgets.PasswordInput(attrs={
                                    "display": "block",
                                    "class": "password1-block css-input",
                                    "placeholder": "Придумайте надежный пароль",
                                }))

    password2 = forms.CharField(label="",
                                max_length=1024,
                                required=True,
                                widget=forms.widgets.PasswordInput(attrs={
                                    "display": "block",
                                    "class": "password2-block css-input",
                                    "placeholder": "Подтвердите пароль",
                                }))


class UpdateLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    username = forms.CharField(label="",
                               max_length=1024,
                               widget=forms.widgets.TextInput(attrs={
                                   "display": "block",
                                   "class": "username-block css-input",
                                   "helptext": "",
                               }))

    email = forms.CharField(label="",
                            max_length=1024,
                            required=False,
                            widget=forms.widgets.TextInput(attrs={
                                "display": "block",
                                "class": "email-block css-input",
                                "helptext": "",
                            }))


class UpdateTextForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['text']

    text = forms.CharField(label="",
                           max_length=1024,
                           widget=forms.widgets.TextInput(attrs={
                               "display": "block",
                               "class": "big-text-block css-input",
                               "helptext": "",
                           }))


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    image = forms.ImageField(label="Загрузить фото", widget=forms.FileInput)


class AddUrl(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['first_url', 'second_url']

    first_url = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                "display": "block",
                                "class": "css-input url-link",
                                "placeholder": "Введите вашу ссылку",
                                }))

    second_url = forms.CharField(widget=forms.widgets.TextInput(attrs={
        "display": "block",
        "class": "css-input url-link",
        "placeholder": "Введите имя для ссылки",
    }))
