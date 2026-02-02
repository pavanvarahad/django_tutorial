from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    task_name = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)