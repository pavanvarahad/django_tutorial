from django.db import models

# Create your models here.
class Todo(models.Model):
    # id = models.BigIntegerField(primary_key=True,auto_created=True)
    id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=300)
    is_completed = models.BooleanField()