from django.db import models
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import Group, User
from email.mime.text import MIMEText

class Root(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=timezone.now)
    
    #to save the data
    def register(self):
        self.save()
        group = Group.objects.get(name = 'Administrador')
        user = User.objects.get(username = self.username)
        group.user_set.add(user)
        #self.send_email()
       
    def send_email(self):
        # Dirección de correo electrónico del destinatario
        destinatario = self.email

        # Asunto del correo electrónico
        asunto = 'Bienvenido a nuestra plataforma'

        # Contenido del correo electrónico
        mensaje = 'Hola {},\n\nBienvenido a nuestra plataforma. Gracias por registrarte.'.format(self.username)

        # Configurar el mensaje como MIMEText y especificar la codificación UTF-8
        mensaje_mime = MIMEText(mensaje, _charset='utf-8')

        # Crear un objeto EmailMessage y configurar los campos
        email = EmailMessage(asunto, mensaje_mime.as_string(), settings.EMAIL_HOST_USER, [destinatario])
        email.content_subtype = 'html'  # Opcional, si el contenido es HTML

        # Establecer la codificación UTF-8 para el correo electrónico
        email.encoding = 'utf-8'

        # Envía el correo electrónico
        email.send()

    class Meta:
        db_table = 'auth_user'
        managed = False
    