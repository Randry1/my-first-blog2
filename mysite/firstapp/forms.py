from calendar import format

from django import forms
from django.core.validators import validate_slug


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', required=True, initial="Патрик")
    age = forms.IntegerField(label='Возраст', initial='4')
    sex = forms.BooleanField(label='Пол', initial=True)
    email_send = forms.NullBooleanField(label='Подписка', required=False)
    email = forms.EmailField(label='Емайл', initial='adf@dasd.d')
    combo = forms.ComboField(fields=[age, sex], initial='sdf sad')
    multi = forms.MultiValueField(fields=[email, name], initial='asdf')
    file = forms.FileField(label='Документ')
    image = forms.ImageField(label='Аватар')
    date = forms.DateTimeField(label='Дата рождения', help_text='Должно быть чило')
    decimal = forms.DecimalField(label='Счет')
    hair_lengh = forms.FloatField(label='Длинна прически')
    foot_size = forms.ChoiceField(label='Размер ноги', choices=(
        (1, "L"),
        (2, "XL"),
        (3, "XXL"),
        (4, "XXXL"),
    ))
    capcha = forms.IntegerField(label="2+2", label_suffix='=')


class HelperTextContactForm(forms.Form):
    '''Форма для изучения аргумента helper_text'''
    subject = forms.CharField(help_text='Не более 100 символов', initial='How a you?')
    message = forms.CharField(initial='Text message', error_messages={'required': 'Мое сообщение об ошибке'})
    sender = forms.EmailField(help_text='Емайл адрес', initial='DFSs@df.dd')
    cc_my_self = forms.BooleanField(required=False, initial=True)  # required=False - отключает проверку
    basket = forms.BooleanField(label='Положить в корзину')
    leave = forms.NullBooleanField(label='Вы поедете в Сочи в этом году?')


class CharFieldForm(forms.Form):
    '''Form for charfield'''
    name = forms.CharField(label='Имя', max_length=6, min_length=2, help_text='Не более 6 символов')
    email = forms.EmailField(label='Емайл', help_text='Обязательно должен быть символ @')
    message = forms.CharField(initial='Text message', widget=forms.Textarea)
    ip_address = forms.GenericIPAddressField(label='IP адрес', help_text='Пример формата 192.168.9.1',
                                             initial='192.168.9.1')
    reg_text = forms.RegexField(label='Регулярные выражения', regex='[0-9][A-F][0-9]')
    field_order = ["name", "email", "ip_address", "reg_text", "message"]  # Регулирование порядка вывода полей


class SlugFieldForm(forms.Form):
    """Example from book SlugFieldForm"""
    slug = forms.SlugField(label='Slug field', required=True, min_length=5, validators=[validate_slug])


class UrlFieldForm(forms.Form):
    """URL Field example book"""
    url_field = forms.URLField(label='Url', help_text='Например http://www.google.com')


class UuiFieldForm(forms.Form):
    """Uui Field form"""
    uui = forms.UUIDField(label="UUI")


class ComboFieldForm(forms.Form):
    """Combo Field Form"""
    combo_text = forms.ComboField(label='Введите текст', fields=[forms.URLField(), forms.CharField(max_length=20)])
