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
    path('url_field_form/', views.url_field_form, name='url_field_form'),
    path('uuid_field_form/', views.uuid_field_form, name='uuid_field_form'),
    path('combo_field_form/', views.combo_field_form, name='combo_field_form'),
    path('file_path_field_form/', views.file_path_field_form, name='file_path_field_form'),
    path('file_field_form/', views.file_field_form, name='file_field_form'),
    path('date_field_form/', views.date_field_form, name='date_field_form'),
    path('time_field_form/', views.time_field_form, name='time_field_form'),
    path('date_time_field_form/', views.date_time_field_form, name='date_time_field_form'),
    path('widget_form/', views.widget_form, name='widget_form'),
    path('thin_tincture_form/', views.thin_tincture_form, name='thin_tincture_form'),
    path('user_book_form/', views.user_book_form, name='user_book_form'),
    path('css_class_form/', views.css_class_form, name='css_class_form'),
    path('attrs_css_form/', views.attrs_css_form, name='attrs_css_form'),
    path('create_person/', views.create_person, name='create_person'), # начало модели
    path('method_get_person/<int:id>/', views.method_get_person, name='method_get_person'), # метод get модели
    path('method_get_or_create_person/', views.method_get_or_create_person, name='method_get_or_create_person'), # метод get_or_create модели
    path('method_filter_person/', views.method_filter_person, name='method_filter_person'), # метод method_filter_person модели
    path('method_exclude_model/', views.method_exclude_model, name='method_exclude_model'), # метод method_exclude_person модели
    path('method_in_bulk_model/', views.method_in_bulk_model, name='method_in_bulk_model'), # метод method_in_bulk_person модели
    path('change_date_in_bd/', views.change_date_in_bd, name='change_date_in_bd'), # метод save модели
    path('update_bd_person/', views.update_bd_person, name='update_bd_person'), # метод save модели
    path('metod_f/', views.metod_f, name='metod_f'), # метод save модели
    path('metod_filter_update/', views.method_filter_update, name='metod_filter_update'), # метод filter(id=1).update() модели
    path('method_filter_update_and_f/', views.method_filter_update_and_f, name='method_filter_update_and_f'), # метод filter(id=1).update() модели
    path('method_update_or_create/', views.method_update_or_create, name='method_update_or_create'), # метод filter(id=1).update() модели
    path('person/<int:id_person>/delete/', views.method_delete_person, name='method_delete_person'), # удаление данных из модели
    path('index_persons', views.index_persons, name='index_persons'), # удаление данных из модели
]
