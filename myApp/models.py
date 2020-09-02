from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    desc = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name