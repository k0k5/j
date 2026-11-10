from django import forms
from .models import Birthday
from django.db import models                     
from django.core.exceptions import ValidationError


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )

    class Meta:
        model = Birthday
        fields = '__all__'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),)       
        widgets ={
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
