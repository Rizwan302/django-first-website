from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timesp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author

class BlockComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.comment[0:10]}... by {self.user}"
    

    