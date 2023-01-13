from django.db import models


# Create your models here.

class MyProject(models.Model):
    sno = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='static/static_dirs/img', default="")
    bag = models.CharField(max_length=20, default="None")
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timesp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.author + ' ' + self.title