from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_description(self):
        return self.description[:75]+'...'

