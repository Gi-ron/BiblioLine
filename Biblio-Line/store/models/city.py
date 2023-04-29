from django.db import models


class City(models.Model):
    name= models.CharField(max_length=100)

    @staticmethod
    def get_all_cities():
        return City.objects.all()


    def __str__(self):
        return self.name