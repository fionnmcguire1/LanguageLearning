from django.urls import path
from . import views

urlpatterns = [
    path('workout-detail/<int:pk>', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('workout-list', views.WorkoutListView.as_view(), name='workout-list')

]
