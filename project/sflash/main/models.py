from django.db import models

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mfile = models.FileField(upload_to='mfiles')

    def __str__(self):
        return self.name