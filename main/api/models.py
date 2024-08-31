from django.db import models


# Create your models here.
class dividedByZero(models.Model):
    timesDividedByZero = models.IntegerField(default=0)

    def __str__(self):
        return f"Number of times someone has divided by zero: {self.timesDividedByZero}"
