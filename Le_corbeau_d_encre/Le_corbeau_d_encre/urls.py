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
from authentication import views as a_views

urlpatterns = [
    path('admin', admin.site.urls),

    # Paths for Okohorn application :
    # Paths to access at home page.
    path('', o_views.home),
    path('okohorn', o_views.home),
    #  Path to acces at Völva page.
    path('volva', o_views.volva, name="volva"),
    # Path to acces at contact page.
    path('contact-us', o_views.contact, name="contact"),

    # Paths for Customer file application :
    # Path to access at home page.
    path('home', cf_views.home, name="home_custom"),
    # Paths about login, logout and inscription.
    path('new_custom', a_views.signup_page, name="inscription"),
    path('custom_login', a_views.login_page, name='login'),
    path('custom_logout', a_views.logout_user, name='logout'),
    # Path for user page.
    path('user_page', cf_views.user_page, name='user'),
    # Path for choices for appointement.
    path('choices', cf_views.choices, name='choices'),
    path('new_project', cf_views.new_project, name='new_project'),
    path('height', cf_views.height, name='height'),
    path('style', cf_views.style, name='style'),
]
