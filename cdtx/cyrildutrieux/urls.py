from django.urls import include, path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', homePage),
]

