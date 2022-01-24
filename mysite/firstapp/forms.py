import os
from calendar import format

from django import forms
from django.core.validators import validate_slug
from django.forms import ModelForm, TextInput
from .models import Electric, Forest, Tree, Bug, Bush


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


class FilePathFieldForm(forms.Form):
    """File path Field, возвращает строку путь к файлу или папку от корня"""
    file_path = forms.FilePathField(label='Выберети файл',
                                    path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                    allow_files=True, allow_folders=True)


class FileFieldForm(forms.Form):
    """File field Поле FileField предназначено для выбора и загрузки файлов и по умолчанmо
    использует виджет ClearabeFileinput с пустым значением None. Поде формирует
    объект UploadedFile, который упаковывает содержимое файла и имя файла в один
    объект. Поле принимает два необязательных аргумента для проверки длины вводи­
    мой строки: max_length (гарантирует, что имя файла не превысит максимальную
    заданную длину) и allow_empty_file (гарантирует, что проверка пройдет успешно,
    даже если содержимое файла пустое)."""
    file = forms.FileField(label='Файл', allow_empty_file=True)

class DateFieldForm(forms.Form):
    """Date field"""
    date = forms.DateField(label="Дата", help_text='Пример 25/12/2021')
    
    
class TimeFieldForm(forms.Form):
    """Time field form"""
    time = forms.TimeField(label='Время: ')

class DateTimeFieldForm(forms.Form):
    """Date time field"""
    # TODO Надо разобраться с провенркой количество заков после запятоай max_whole_digits у DecimalField. Что это вообще такое
    date_time = forms.DateTimeField(help_text='например, 2021-12-25 14: 30: 59 иnи 25/12/2021 14: 30')
    duration = forms.DurationField(label='Введите промежуток времени',
                                   help_text='"DD нн:мм:SS" -например, 2 1:10:20 (2 дня 1 час 10 минут 20 секунд)')
    split_date = forms.SplitDateTimeField(label='Введите дату и время')
    integer_field = forms.IntegerField(label='Введите целое число:')
    decimal_field = forms.DecimalField(label='Введите число с точкой', max_value=100.0, min_value=0.0, decimal_places=2)
    float_field = forms.FloatField(label='Введите число с плавающей точкой')  # Непонятно чем отличается от decimal
    choice = forms.ChoiceField(choices=((1, 'Английский'),
                                        (2, 'Немецкий'),
                                        (3, 'Французкий')))
    # TODO Узнаить как работает coerce= в TypeChoice
    type_choice = forms.TypedChoiceField(label='Выберете город', empty_value=None, choices=((1, 'Москва'),
                                                                                            (2, 'Воронеж'),
                                                                                            (3, 'Курск')), )
    multiple_choice = forms.MultipleChoiceField(label='Выберете город',
                                                choices=((1, 'Москва'),
                                                         (2, 'Воронеж'),
                                                         (3, 'Курск')))
    # Как я понял это тотже Multiple только можно свои проверки на валидацию делать
    type_multiple_choice = forms.TypedMultipleChoiceField(label='Выберете город',
                                                          choices=((1, 'Москва'),
                                                                   (2, 'Воронеж'),
                                                                   (3, 'Курск')),
                                                          empty_value=None)


class WidgetForm(forms.Form):
    """Форма для проверки как работают виджеты в формах"""
    name = forms.CharField(label='Имя:', initial='Витя')
    age = forms.IntegerField(label='Возраст', initial='46', help_text='Введите ваш возраст')
    comment = forms.CharField(label='Комментарий:', widget=forms.Textarea, initial='Комментарий')
    ad = forms.BooleanField(label='Согласны получать рекламу?', required=False)


class ThinTinctureForm(forms.Form):
    """Тонкая настройка формы"""
    # TODO добавить класс css через виджет https://docs.djangoproject.com/en/dev/ref/forms/widgets/#django.forms.Widget.attrs
    name = forms.CharField(label='Имя', initial='Витя', widget=forms.TextInput(attrs={"class": "field_class_from_attrs"}))
    age = forms.IntegerField(label='Возраст', initial='46', help_text='Введите ваш возраст', widget=forms.NumberInput(attrs={"class": "field_class_from_attrs"}))
    comment = forms.CharField(label='Комментарий')


class UserBookForm(forms.Form):
    """Форма для учебника тонкая настройка"""
    name = forms.CharField(label="Имя:")
    age = forms.IntegerField(label="Возраст:")
    required_css_class = 'field'
    field_css_class = "fortuna"
    error_css_class = 'error'           #Отображается в классе который оборачиевает input и label добовляется только если форма не прошла валидацию


class CreatePerson(forms.Form):
    """Форма для заполнения модели персоны"""
    is_create = forms.BooleanField(label="Создать запрись в таблице firstapp_person?")


class ChangeDataPersonModel(forms.Form):
    """ Меняем данные модели Person из формы """
    id_person = forms.IntegerField()
    name = forms.CharField()
    age = forms.CharField()
    only_name = forms.BooleanField(label='Изменить только имя: ', required=False)


class UpdateColumnForm(forms.Form):
    """Форма для добавлени всем персонам вадраста в столбец"""
    delta_age = forms.IntegerField(label='Добавить возраст на:')


class UpdatePerson(forms.Form):
    """Форма для обновления данных в модели"""
    id_person = forms.IntegerField(label='id:')
    name = forms.CharField(label='Имя:', required=False)
    age = forms.IntegerField(label='Возраст', required=False)
    bio = forms.CharField(label='Описание:', required=False)


class DeletePerson(forms.Form):
    """Форма для удаление данных методом post запроса"""
    id_person = forms.IntegerField(label='Id', widget=forms.HiddenInput)
    

class ElectricForm(ModelForm):
    """Форма для модели электрика"""
    class Meta:
        model = Electric
        fields = '__all__'

class ForestForm(ModelForm):
    """Форма для модели лес"""
    class Meta:
        model = Forest
        fields = '__all__'

class TreeForm(ModelForm):
    """Форма для модели дерево"""
    class Meta:
        model = Tree
        fields = '__all__'

class TreeFormM(ModelForm):
    """Попробую настроить форму через виджеты"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['forest'].widget.attrs.update({'class': 'hidden hide_parents' })
        self.fields['forest'].label = False

    class Meta:
        model = Tree
        fields = ['forest', 'name', 'height']
        # widgets ={
        #     'name': TextInput(attrs={
        #                    'class': 'form-control',
        #                    'placeholder': 'Название леса '
        #                     })
        # }


class BugForm(ModelForm):
    """Form bug model"""
    class Meta:
        model = Bug
        fields = '__all__'


class BushForm(ModelForm):
    """Bush form fo model bush"""
    bug_id = forms.CharField(required=False)
    class Meta:
        model = Bush
        fields =  ['name']

class BushFormForEdit(ModelForm):
    """Куст форма для изиенение куста"""
    # def __init__(self, *args, **kwargs):
    #     super.__init__(*args, **kwargs)
    #     self.fields['bug'].widget.attrs.update({'class': 'hidden'})
    class Meta:
        model = Bush
        fields = '__all__'

class AddBushInBug(forms.Form):
    """Форма добовляет куст к жуку"""
    bushes = Bush.objects.all()
    CHOICES = []
    for bush in bushes:
        CHOICES.append( (bush.id, (bush.name + " " + str(bush.id) )))
    bush_id = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label='Добавить куст')


class BugBushClear(forms.Form):
    """Форма чтобы прердать по пост запросу откреплене жука от куста"""
    bush_id = forms.IntegerField(show_hidden_initial=False,required=False)