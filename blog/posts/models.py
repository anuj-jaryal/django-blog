from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{ self.user.username} Post'

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk':self.pk})
    

