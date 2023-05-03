from django.db import models

class Country(models.Model):
    name= models.CharField(max_length=100)


    @staticmethod
    def get_all_countreis():
        return Country.objects.all()


    def __str__(self):
        return self.name
