from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('about/',views.about, name='about'),
    re_path(r'^about', views.about),
    path('contact/',views.contact, name='contact'),
    path('', views.index, name='index'),
    path('products/<int:productid>/', views.products, name='products'),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    #r'^*началозапроса* blank*название функуии во views.py /(?P<blankid>\d+)*описания переменных*/(?P<name>\D+)/(?P<phone>\d+)/'
    re_path(r'^blanks/(?P<blankid>\d+)/(?P<name>\D+)/(?P<phone>\d+)/', views.blanks, name='blanks'),
]