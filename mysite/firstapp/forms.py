from calendar import format

from django import forms


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
    subject = forms.CharField(help_text='Не более 100 символов')
    message = forms.CharField()
    sender = forms.EmailField(help_text='Емайл адрес')
    cc_my_self = forms.BooleanField(required=False)
