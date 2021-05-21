from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=45,null=False)
    description=models.TextField(null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
