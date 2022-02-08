from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    # path('books/', views.books, name='books'),
]