from django.db import models

# Create your models here.
class Direction(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)

class Classify(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    direction = models.ForeignKey(to='Direction', to_field='id', null=False, on_delete=models.CASCADE)

class Difficulty(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)

class Course(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    introduce = models.TextField(null=True)
    notice = models.TextField(null=True)
    course_icon = models.CharField(max_length=255, null=False)
    integral = models.IntegerField(default=0, null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    classify = models.ForeignKey(to='Classify', to_field='id', null=False, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(to='Difficulty', to_field='id', null=False, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to='user.Teacher', to_field='id', null=False, default=1, on_delete=models.CASCADE)
    pre_course = models.ForeignKey(to='Course', to_field='id', null=True, on_delete=models.CASCADE)


class Chapter(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    introduce = models.TextField(null=True)
    course = models.ForeignKey(to='Course', to_field='id', null=False, on_delete=models.CASCADE)

class Video(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    video_src = models.CharField(null=False, max_length=255)
    video_time = models.TimeField(null=False)
    chapter = models.ForeignKey(to='Chapter', to_field='id', null=False, on_delete=models.CASCADE)

class Courseware(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    content = models.TextField(null=False)
    courseware_time = models.TimeField(null=False)
    chapter = models.ForeignKey(to='Chapter', to_field='id', null=False, on_delete=models.CASCADE)

