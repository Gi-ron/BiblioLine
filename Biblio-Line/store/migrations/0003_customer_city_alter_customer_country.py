# Generated by Django 4.2.1 on 2023-05-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_city_idcountry_alter_city_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=250),
        ),
    ]
