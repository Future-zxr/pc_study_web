from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(unique=True, null=False, max_length=255)
    content_html = models.TextField(null=False)
    content_editor = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='user.User', to_field='id', null=False, on_delete=models.CASCADE)
    classify = models.CharField(max_length=255, null=False)
    mold = models.CharField(max_length=255, null=True)
