from django.db import models

class places(models.Model):
    images = models.ImageField(upload_to='data/img',null=True,blank=True)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    def __str__(self):
        return self.title