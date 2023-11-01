from django.db import models

# Create your models here.
class dynamicCode(models.Model):
    dynamicCode = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dynamicCode