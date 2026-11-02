from django.shortcuts import render
from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request):
    if request.POST:
        form = BirthdayForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            birthday_countdown = calculate_birthday_countdown(
                form.cleaned_data['birthday']
            )
            context.update({'birthday_countdown': birthday_countdown})
    else:
        form = BirthdayForm()
        context = {'form': form}

    
    return render(request, 'birthday/birthday.html', context=context)

def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)

def edit_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)  
    form = BirthdayForm(request.POST or None, instance=instance)

    context = {'form': form}

    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birtgday/birtgday.html', context)