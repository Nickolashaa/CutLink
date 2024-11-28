from django.urls import path
from . import views as shop_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', shop_views.home, name="home"),
    path('about/', shop_views.about, name="about"),
    path('reg/', shop_views.reg, name="reg"),
    path('auth/', auth_views.LoginView.as_view(template_name="shop/auth.html"), name="auth"),
    path('exit/', auth_views.LogoutView.as_view(template_name="shop/exit.html"), name="exit"),
    path('profile/', shop_views.profile, name="profile"),
    path('urls/', shop_views.urls, name="urls"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)