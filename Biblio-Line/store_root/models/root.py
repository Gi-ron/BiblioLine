from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone

class Root(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=timezone.now)
    
    #to save the data
    def register(self):
        self.save()
        #self.send_email()
       
    def send_email(self):
        asunto = 'Ha sido registrado en Biblio Line'
        mensaje = 'Bienvenido a Bilibo Line !Ingrese con su DNI y cambie su contraseña¡'
        destinatarios = [self.email]
        
        send_mail(asunto, mensaje, settings.DEFAULT_FROM_EMAIL, destinatarios)
        
    class Meta:
        db_table = 'auth_user'
        managed = False
    