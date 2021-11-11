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
    re_path(r'^mod_products/$', views.mod_products, name='mod_products'),
    re_path(r'^mod_products/(?P<productid>\d+)/', views.mod_products, name='mod_products'),
    path('posts/', views.posts),
    path('posts/<int:id>/', views.posts),
    path('posts/<int:id>/edit/', views.posts_edit),
    path('posts/<int:id>/<str:name>/', views.posts_name),
    path('detail/', views.detail),
]