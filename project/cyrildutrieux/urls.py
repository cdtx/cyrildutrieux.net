"""cyrildutrieux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf import settings
from django.urls import include, path,re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

handler400 = 'cdtx.django_error_handlers.views.handler400'
handler403 = 'cdtx.django_error_handlers.views.handler403'
handler404 = 'cdtx.django_error_handlers.views.handler404'
handler500 = 'cdtx.django_error_handlers.views.handler500'

urlpatterns = [
    re_path(r'^admin/', include('django.contrib.auth.urls')),
    path(r'easy_password/', include('cdtx.django_easy_password.urls')),
    re_path(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^', include('cdtx.cyrildutrieux.urls')),
]
