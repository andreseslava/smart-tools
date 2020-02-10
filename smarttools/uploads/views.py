from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

# from contests.models import Contest
from uploads.forms import UploadForm
from .models import Video
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return HttpResponseRedirect('/uploads')
    else:
        form = UploadForm();

    return render(request, 'contests/contest.html', {'form': form})


class UploadDetailForm(CreateView):
    model = Video
    success_url = reverse_lazy('contest_test_home')
    fields = ['title', 'description', 'name', 'sureName', 'email']
