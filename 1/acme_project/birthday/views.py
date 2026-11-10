from django.shortcuts import render
from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

class BirthdayList(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

# ===========================================#

# class BirthdayMixin:
#     model = Birthday
#     success_url = reverse_lazy('birthday:list')

# ===========================================#

class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context

# ===========================================#

class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm

# ===========================================#

class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm

# ===========================================#

class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')

# ===========================================#


# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.all()
#     # Передаём их в контекст шаблона.
#     context = {'birthdays': birthdays}
#     return render(request, 'birthday/birthday_list.html', context)


# def birthday(request):
#     if request.POST:
#         form = BirthdayForm(request.POST)
#         context = {'form': form}
#         if form.is_valid():
#             form.save()
#             birthday_countdown = calculate_birthday_countdown(
#                 form.cleaned_data['birthday']
#             )
#             context.update({'birthday_countdown': birthday_countdown})
#     else:
#         form = BirthdayForm()
#         context = {'form': form}

    
#     return render(request, 'birthday/birthday.html', context=context)

# def edit_birthday(request, pk):
#     instance = get_object_or_404(Birthday, pk=pk)  
#     form = BirthdayForm(request.POST or None, instance=instance)

#     context = {'form': form}

#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context)

# def delete_birthday(request, pk):
#     # Получаем объект модели или выбрасываем 404 ошибку.
#     instance = get_object_or_404(Birthday, pk=pk)
#     # В форму передаём только объект модели;
#     # передавать в форму параметры запроса не нужно.
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     # Если был получен POST-запрос...
#     if request.method == 'POST':
#         # ...удаляем объект:
#         instance.delete()
#         # ...и переадресовываем пользователя на страницу со списком записей.
#         return redirect('birthday:list') # <--- импортируем
#     # Если был получен GET-запрос — отображаем форму.
#     return render(request, 'birthday/birthday.html', context)
