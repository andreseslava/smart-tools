from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContestForm


def contest(request):
    if request.method == 'POST':
        form = ContestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/uploads')

    else:
        form = ContestForm();

    return render(request, 'contests/contest.html', {'form': form})
