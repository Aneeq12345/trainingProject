from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField
# Create your models here.
class tasks(models.Model):
    title =models.CharField(max_length=100)
    description=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField()
    completion_date=models.DateTimeField(null=True,blank=True)
    completion_status=models.BooleanField(default=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    attach_files=models.JSONField(null=True)

    def __str__(self):
        return self.title

