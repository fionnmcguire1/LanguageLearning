from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from . import models
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Gym Tracker index.")


class WorkoutDetailView(DetailView):

    model = models.Workout
    #template_name = 'templates/workout_detail.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['now'] = timezone.now()
            return context

class WorkoutListView(ListView):

    model = models.Workout
    #template_name = 'templates/workout_list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['now'] = timezone.now()
            return context
