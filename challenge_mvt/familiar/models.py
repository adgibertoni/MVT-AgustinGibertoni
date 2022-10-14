from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField()
    fav_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} | Fecha de nacimiento: {self.birth_date} | Lucky number: {self.fav_number}"
