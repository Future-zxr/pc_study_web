from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    tel = models.CharField(null=False,unique=True,max_length=11)
    email = models.EmailField(null=True,max_length=255)
    psw = models.CharField(null=False,max_length=255)
    register_time = models.DateTimeField(auto_now_add=True)

class Sex(models.Model):
    name = models.CharField(null=False,unique=True,max_length=255)

class Icon(models.Model):
    icon_img = models.CharField(null=False,unique=True,max_length=255)

class UserInfo(models.Model):
    user_name = models.CharField(null=False,unique=True,max_length=255)
    user_icon = models.ForeignKey(to='Icon', to_field='id', default=1, null=False, on_delete=models.CASCADE)
    user_sex = models.ForeignKey(to='Sex', to_field='id', default=1, null=False, on_delete=models.CASCADE)
    identity = models.CharField(null=True, max_length=255)
    address = models.CharField(null=True, max_length=255)
    introduce = models.TextField(null=True)
    user = models.ForeignKey(to='User', to_field='id', null=False, on_delete=models.CASCADE)

class CheckIn(models.Model):
    check_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='User', to_field='id', null=False, on_delete=models.CASCADE)

class UserIntegral(models.Model):
    integral = models.IntegerField(null=False)
    user = models.ForeignKey(to='User', to_field='id', null=False, on_delete=models.CASCADE)
    get_date = models.DateTimeField(auto_now_add=True)

# 老师
class TeacherIdentity(models.Model):
    identity = models.CharField(null=False, unique=True, max_length=255)

class Teacher(models.Model):
    name = models.CharField(null=False, unique=True, max_length=255)
    introduce = models.TextField(null=True)
    teacher_icon = models.ForeignKey(to='Icon', to_field='id', default=1, null=True, on_delete=models.CASCADE)
    teacher_sex = models.ForeignKey(to='Sex', to_field='id', default=1, null=False, on_delete=models.CASCADE)
    teacher_identity = models.ForeignKey(to='TeacherIdentity', to_field='id', null=False, on_delete=models.CASCADE)



