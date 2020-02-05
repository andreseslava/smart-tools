from django.conf.urls import url
from django.urls import path

from . import views
from .models import Contest

urlpatterns = [

    # url(r'^$', views.contest),
    url('contest_list', views.ContestListView.as_view(model=Contest), name='contest-list'),
    path('contest/<int:pk>/update/', views.ContestUpdateView.as_view(model=Contest), name='contest-update'),
    path('contest/<int:pk>/delete/', views.ContestDeleteView.as_view(model=Contest), name='contest-delete'),
    path('contest/<int:pk>/detail/', views.ContestVideoListView.as_view(model=Contest), name='contest-object-list'),
]
