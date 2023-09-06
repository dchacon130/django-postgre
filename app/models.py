from django.db import models

# Create your models here.
class User(models.Model):
    number = models.IntegerField()
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    birtday = models.DateField()
    language  = models.CharField()
    country  = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
