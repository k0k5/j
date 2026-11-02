from django.shortcuts import render
from .forms import ContestForm


def proposal_create(request):
    return render(request, 'contest/form.html')


def accepted(request):
    return render(request, 'contest/proposal_accepted.html')


def proposal(request):
    form = ContestForm(request.GET or None)
    context = {'form': form}
    return render(request, 'contest/form.html', context)

