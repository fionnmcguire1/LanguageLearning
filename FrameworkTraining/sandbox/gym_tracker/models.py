from django.db import models

class BodyPart(models.Model):
    name = models.CharField(max_length=50)

class Excercise(models.Model):
    name = models.CharField(max_length=200)
    custom = models.BooleanField(default=False)
    body_part = models.ForeignKey(BodyPart,on_delete=models.SET_NULL,null=True)

class Workout(models.Model):
    name = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Excercise)

class Set(models.Model):
    number = models.SmallIntegerField(default=1)
    reps =  models.SmallIntegerField(default=1)
    exercise = models.ForeignKey(Excercise,on_delete=models.SET_NULL,null=True)
    workout = models.ForeignKey(Workout,on_delete=models.SET_NULL,null=True)

class Goal(models.Model):
    goal_number = models.SmallIntegerField(default=1)
    exercise = models.ForeignKey(Excercise,on_delete=models.SET_NULL,null=True)
