from calendar import format

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', required=True)
    age = forms.IntegerField(label='Возраст')
    sex = forms.BooleanField(label='Пол')
    email_send = forms.NullBooleanField(label='Подписка', required=False)
    email = forms.EmailField(label='Емайл')
    combo = forms.ComboField(fields=[age, sex])
    multi = forms.MultiValueField(fields=[email, name])
    file = forms.FileField(label='Документ')
    image = forms.ImageField(label='Аватар')
    date = forms.DateTimeField(label='Дата рождения')
    decimal = forms.DecimalField(label='Счет')
    hair_lengh = forms.FloatField(label='Длинна прически')
    foot_size = forms.ChoiceField(label='Размер ноги', choices=(
        (1, "L"),
        (2, "XL"),
        (3, "XXL"),
        (4, "XXXL"),
    ))
