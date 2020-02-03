from django.http import HttpResponseRedirect
from django.shortcuts import render

from contests.models import Contest
from uploads.forms import UploadForm


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
