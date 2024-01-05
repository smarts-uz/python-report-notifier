from django.db import models

# Create your models here.
class TG(models.Model):
    name = models.CharField(verbose_name="Name",max_length=255)

    def __str__(self):
        return self.name

