from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContestForm
from uploads.models import Video
from .models import Contest
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


class ContestVideoListView(ListView):
    context_object_name = "videos"
    template_name_suffix = '_video_list'
    model = Contest

    def get_queryset(self, *args, **kwargs):
        return Video.objects.filter(contest=self.kwargs['pk'])
        # return Contest.objects.filter(video__contest='this_object_id')


class ContestDeleteView(DeleteView):
    model = ContestForm()
    success_url = reverse_lazy('contest-list')


class ContestUpdateView(UpdateView):
    model = ContestForm
    template_name_suffix = '_update'
    fields = ['name', 'startDate', 'endDate', 'path', 'prize',
              'created_at', 'logo', 'author']
    success_url = reverse_lazy('contest-list')
