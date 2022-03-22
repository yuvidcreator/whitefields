from django.urls import path

from .views import *

app_name = 'store'

urlpatterns = [
    path('', product_all, name='store_home'),
    path('<slug:slug>', product_detail, name='product_detail'),
    path('<slug:category_slug>/', category_list, name='category_list'),

    path('about/', AboutPage, name="about_page"),
    path('contact/', ContactPage, name="contact_page"),
    path('login/', LoginPage, name="Login-Page"),
    path('user/', UserDashPage, name="UserDash-Page"),
]