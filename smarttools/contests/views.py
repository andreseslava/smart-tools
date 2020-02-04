from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import  reverse_lazy
from .forms import ContestForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def contest(request):
    if request.method == 'POST':
        form = ContestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/uploads')

    else:
        form = ContestForm();

    return render(request, 'contests/contest.html', {'form': form})

class ContestListView(ListView):
    model = ContestForm
    context_object_name = "tutorials"

class ContestDeleteView(DeleteView):
    model = ContestForm()
    success_url = reverse_lazy('contest-list')

class ContestUpdateView(UpdateView):
    model = ContestForm
    template_name_suffix = '_update'
    fields = ['name', 'startDate', 'endDate', 'path', 'prize',
              'created_at', 'logo', 'author']
    success_url = reverse_lazy('contest-list')