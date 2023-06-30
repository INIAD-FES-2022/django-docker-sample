from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30, verbose_name="タスク名")
    is_done = models.BooleanField(default=False, verbose_name="完了")
    
    def __str__(self):
        return self.title

