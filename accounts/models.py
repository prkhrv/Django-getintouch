from django.db import models

# Create your models here.
class getintouch(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    company = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    website = models.CharField(max_length=40,blank = True)
    comments = models.TextField(max_length=None,blank=True)

    def __str__(self):
        return self.first_name
