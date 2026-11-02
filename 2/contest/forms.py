# Опишите класс формы здесь!
from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20,
        required=True,
    )
    description = forms.CharField(
        label='Описание',
        required=True,
        widget=forms.Textarea(attrs={'rows': 4}),
    )
    price = forms.IntegerField(
        label='Цена',
        required=True,
        min_value=10,
        max_value=100,
        help_text='Рекомендованная розничная цена',
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4}),
    )

class Contest(forms.Form):
    title = forms.IntegerField()
    description = forms.Textarea()
    comment = forms.Textarea()
    price = forms.IntegerField()
    class Meta:
        fields = '__all__'
        wigets ={
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }    