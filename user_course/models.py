from django.db import models

# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(to='course.Course', to_field='id', null=False, on_delete=models.CASCADE)
    col_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('user', 'course'),)

class SelectCourse(models.Model):
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(to='course.Course', to_field='id', null=False, on_delete=models.CASCADE)
    sc_date = models.DateTimeField(auto_now_add=True)
    iscomplete = models.IntegerField(null=False, default=0)
    class Meta:
        unique_together = (('user', 'course'),)

class CourseEvaluation(models.Model):
    content = models.TextField(null=False)
    course = models.ForeignKey(to='course.Course', to_field='id', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    eva_date = models.DateTimeField(auto_now_add=True)

class UserVideo(models.Model):
    progress = models.TimeField(null=False)
    video = models.ForeignKey(to='course.Video', to_field='id', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('video', 'user'),)


class QuestionVideo(models.Model):
    content = models.TextField(null=False)
    video = models.ForeignKey(to='course.Video', to_field='id', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    question_video = models.ForeignKey(to='QuestionVideo', to_field='id', null=True, on_delete=models.CASCADE)
    qv_date = models.DateTimeField(auto_now_add=True)

class UserCourseware(models.Model):
    iswatch = models.IntegerField(null=False, default=0)
    courseware = models.ForeignKey(to='course.Courseware', to_field='id', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('courseware', 'user'),)

class QuestionCourseware(models.Model):
    content = models.TextField(null=False)
    courseware = models.ForeignKey(to='course.Courseware', to_field='id', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    question_courseware = models.ForeignKey(to='QuestionCourseware', to_field='id', null=True, on_delete=models.CASCADE)
    qc_date = models.DateTimeField(auto_now_add=True)
