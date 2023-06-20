from django.db import models
from django.utils import timezone

class post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class meta :
        ordering=['-publish']

    def __str__(self):
        return self.title
# Create your models here.
