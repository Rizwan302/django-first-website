from django.db import models

# Create your models here.
class Contact(models.Model):
    son = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    content = models.TextField()
    timesp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message form ' + self.name

