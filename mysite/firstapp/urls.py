from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('about/',views.about, name='about'),
    path('about_template/', views.about_template, name='about_template'),
    re_path(r'^about', views.about),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('products/<int:productid>/', views.products, name='products'),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    # r'^*началозапроса* blank*название функуии во views.py /(?P<blankid>\d+)*описания переменных*/(?P<name>\D+)/(?P<phone>\d+)/'
    re_path(r'^blanks/(?P<blankid>\d+)/(?P<name>\D+)/(?P<phone>\d+)/', views.blanks, name='blanks'),
    re_path(r'^mod_products/$', views.mod_products, name='mod_products'),
    re_path(r'^mod_products/(?P<productid>\d+)/', views.mod_products, name='mod_products'),
    path('posts/', views.posts),
    path('posts/<int:id>/', views.posts),
    path('posts/<int:id>/edit/', views.posts_edit),
    path('posts/<int:id>/<str:name>/', views.posts_name),
    path('detail/', views.detail),
    path('m304/', views.m304),
    path('m400/', views.m400),
    path('m403/', views.m403),
    path('m404', views.m404),
    path('template/', views.def_template_render),
    path('app1/', views.index_app1),
    path('app2/', views.index_app2),
    path('contact_template/', TemplateView.as_view(template_name='firstapp/contact_template.html', extra_context={
        "work": "Создание и поддержка сайтов и веб приложений"
    })),
    path('index_app3', views.index_app3, name='app3'),
    path('if_template/', views.if_template, name='if_template'),
    path('for_template/', views.for_template, name='for_template'),
    path('form_template/', views.form_template, name='form_template'),
    path('form_helper_text/', views.form_helper_text, name='form_helper_text'),
    path('form_char_field/', views.form_char_field, name='form_char_field'),
    path('slug_field_form/', views.slug_field_form, name='slug_field_form'),
]
