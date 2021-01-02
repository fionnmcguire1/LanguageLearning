from django.db import models

class BodyPart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    custom = models.BooleanField(default=False)
    body_part = models.ForeignKey(BodyPart,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name

class Set(models.Model):
    number = models.SmallIntegerField(default=1)
    reps =  models.SmallIntegerField(default=1)
    exercise = models.ForeignKey(Exercise,on_delete=models.SET_NULL,null=True)
    workout = models.ForeignKey(Workout,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.number) +' - '+self.exercise.name+' - '+self.workout.name

class Goal(models.Model):
    goal_number = models.SmallIntegerField(default=1)
    exercise = models.ForeignKey(Exercise,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.exercise.name+' - '+str(self.goal_number)
