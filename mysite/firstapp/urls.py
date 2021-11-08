from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # path('about/',views.about, name='about'),
    re_path(r'^about', views.about),
    path('contact/',views.contact, name='contact'),
]