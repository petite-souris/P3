"""Le_corbeau_d_encre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Okohorn import views as o_views
from Customer_file import views as cf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', o_views.home),
    path('okohorn/', o_views.home),
    path('volva/', o_views.volva, name="volva"),
    path('contact-us/', o_views.contact, name='contact'),
    path('home/', cf_views.home, name="home_custom"),
    path('login/', cf_views.login, name="login"),
    path('new_custom/', cf_views.new_custom, name="new_custom")
]
