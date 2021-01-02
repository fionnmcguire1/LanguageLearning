from django.contrib import admin

from gym_tracker.models import Goal, BodyPart, Exercise, Workout, Set


class GoalAdmin(admin.ModelAdmin):
    fields = ['goal_number', 'exercise']

admin.site.register(Goal, GoalAdmin)

class BodyPartAdmin(admin.ModelAdmin):
    fields = ['name',]

admin.site.register(BodyPart, BodyPartAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    fields = ['name', 'custom', 'body_part',]

admin.site.register(Exercise, ExerciseAdmin)

class WorkoutAdmin(admin.ModelAdmin):
    fields = ['name', 'exercises',]

admin.site.register(Workout, WorkoutAdmin)

class SetAdmin(admin.ModelAdmin):
    fields = ['number', 'reps','exercise','workout',]

admin.site.register(Set, SetAdmin)
